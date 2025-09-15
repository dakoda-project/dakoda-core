from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Literal, Callable
import polars as pl

Operator = Literal[
    'eq', 'ne', 'lt', 'le', 'gt', 'ge',
    'contains', 'startswith', 'endswith',
    'in', 'not_in', 'is_null', 'is_not_null', 'custom'
]

OPERATOR_FUNCTIONS = {
    'eq': lambda series, value: series == value,
    'ne': lambda series, value: series != value,
    'lt': lambda series, value: series < value,
    'le': lambda series, value: series <= value,
    'gt': lambda series, value: series > value,
    'ge': lambda series, value: series >= value,
    'contains': lambda series, value: series.str.contains(str(value), literal=True),
    'startswith': lambda series, value: series.str.starts_with(str(value)),
    'endswith': lambda series, value: series.str.ends_with(str(value)),
    'in': lambda series, value: series.is_in(value),
    'not_in': lambda series, value: ~series.is_in(value),
    'is_null': lambda series, value: series.is_null(),
    'is_not_null': lambda series, value: series.is_not_null(),
    'custom': lambda series, value: series.map_elements(value, return_dtype=pl.Boolean)
}

numeric_operators = {'lt', 'le', 'gt', 'ge'}

AggregationFunction = Literal['count', 'sum', 'mean', 'min', 'max', 'std', 'var']

AGGREGATION_FUNCTIONS = {
    'count': lambda value_col: pl.len(),
    'sum': lambda value_col: pl.col(value_col).sum(),
    'mean': lambda value_col: pl.col(value_col).mean(),
    'min': lambda value_col: pl.col(value_col).min(),
    'max': lambda value_col: pl.col(value_col).max(),
    'std': lambda value_col: pl.col(value_col).std(),
    'var': lambda value_col: pl.col(value_col).var()
}

numeric_aggregations = {'sum', 'mean', 'min', 'max', 'std', 'var'}

class Predicate(ABC):
    """Base predicate that returns a boolean series indicating which rows match"""

    @abstractmethod
    def evaluate(self, df: pl.DataFrame) -> pl.Series:
        """Return a boolean series indicating which rows match this predicate"""
        pass

    def filter(self, df: pl.DataFrame) -> pl.DataFrame:
        """Filter dataframe rows based on the predicate"""
        mask = self.evaluate(df)
        return df.filter(mask)

    def documents(self, df: pl.DataFrame, idx_col='idx') -> pl.Series:
        """Get unique document indices that match the predicate"""
        filtered = self.filter(df)
        if len(filtered) == 0:
            return pl.Series([], dtype=pl.Int64)
        return filtered[idx_col].unique().sort()


    def __and__(self, other: Predicate) -> AndPredicate:
        return AndPredicate([self, other])

    def __or__(self, other: Predicate) -> OrPredicate:
        return OrPredicate([self, other])

    def __invert__(self) -> NotPredicate:
        return NotPredicate(self)


class TruePredicate(Predicate):
    """Always returns True for all rows"""

    def evaluate(self, index: pl.DataFrame) -> pl.Series:
        return pl.repeat(True, n=len(index), dtype=pl.Boolean, eager=True)


class FalsePredicate(Predicate):
    """Always returns False for all rows"""

    def evaluate(self, index: pl.DataFrame) -> pl.Series:
        return pl.repeat(False, n=len(index), dtype=pl.Boolean, eager=True)


def _infer_cast_type(value: Any):
    """Infer the Polars data type to cast to based on the comparison value"""
    if isinstance(value, str):
        return pl.String
    elif isinstance(value, (int, float)):
        return pl.Float64
    elif isinstance(value, bool):
        return pl.Boolean
    elif isinstance(value, list) and value:
        return _infer_cast_type(value[0])
    return None

def _safe_convert(converter):
    def wrapper(x):
        if x is None:
            return None
        try:
            return converter(x)
        except (ValueError, TypeError):
            return None

    return wrapper

def _cast_safe(series: pl.Series, cast_type: pl.DataType) -> pl.Series:
    """Tries to cast a polars series to the given datatype."""
    converters = {
        pl.String: _safe_convert(str),
        pl.Float64: _safe_convert(float),
        pl.Boolean: _safe_convert(bool),
    }

    if series.dtype == pl.Object or cast_type in converters:
        if cast_type in converters:
            return series.map_elements(converters[cast_type], return_dtype=cast_type)

    try:
        return series.cast(cast_type, strict=False)
    except pl.ComputeError:
        # Triangle cast: original → string → target
        string_series = series.map_elements(converters[pl.String], return_dtype=pl.String)
        return string_series if cast_type == pl.String else string_series.cast(cast_type, strict=False)


@dataclass
class ColumnPredicate(Predicate):
    """Predicate that checks a specific column against a condition"""
    column: str
    operator: Operator
    value: Any

    def evaluate(self, df: pl.DataFrame) -> pl.Series:
        if self.column not in df.columns:
            return FalsePredicate().evaluate(df)

        series = df[self.column]
        op_fn = OPERATOR_FUNCTIONS[self.operator]

        cast_type = _infer_cast_type(self.value)
        if cast_type is not None:
            series = _cast_safe(series, cast_type)

        if self.operator not in ['is_null', 'is_not_null']:
            return df.select(
                pl.when(series.is_not_null())
                .then(op_fn(series, self.value))
                .otherwise(False)
            ).to_series()
        else:
            return op_fn(series, self.value)

@dataclass
class CompositePredicate(Predicate):
    predicates: list[Predicate]
    conjunction_type: Literal['and', 'or'] = 'and'

    def __post_init__(self):
        if self.conjunction_type not in ['and', 'or']:
            self.conjunction_type = 'and'

    def evaluate(self, df: pl.DataFrame) -> pl.Series:
        if not self.predicates:
            val = True if self.conjunction_type == 'and' else False
            return pl.repeat(val, n=len(df), dtype=pl.Boolean, eager=True)

        result = self.predicates[0].evaluate(df)
        for pred in self.predicates[1:]:
            if self.conjunction_type == 'and':
                result = result & pred.evaluate(df)
            else:
                result = result | pred.evaluate(df)
        return result


@dataclass
class AndPredicate(CompositePredicate):
    """Combines predicates with AND logic"""

    def __init__(self, predicates: list[Predicate]):
        super().__init__(predicates, 'and')


@dataclass
class OrPredicate(CompositePredicate):
    """Combines predicates with OR logic"""

    def __init__(self, predicates: list[Predicate]):
        super().__init__(predicates, 'or')


@dataclass
class NotPredicate(Predicate):
    """Negates a predicate"""
    predicate: Predicate

    def evaluate(self, df: pl.DataFrame) -> pl.Series:
        return ~self.predicate.evaluate(df)


@dataclass
class AggregationPredicate(Predicate):
    """Predicate that filters documents based on aggregated values"""
    base_predicate: Predicate
    agg_function: AggregationFunction
    operator: Operator
    threshold: Any
    group_by: str = 'idx'
    value_column: str = 'value'

    def evaluate(self, df: pl.DataFrame) -> pl.Series:
        """Return boolean series indicating which documents pass the aggregation filter"""
        # First filter by base predicate
        filtered = self.base_predicate.filter(df)

        if len(filtered) == 0:
            return FalsePredicate().evaluate(df)

        if self.agg_function not in AGGREGATION_FUNCTIONS:
            raise ValueError(f"Unknown aggregation function: {self.agg_function}")

        if self.agg_function in numeric_aggregations:
            filtered = filtered.with_columns(pl.col(self.value_column).cast(pl.Float64, strict=False))

        agg_expr = AGGREGATION_FUNCTIONS[self.agg_function](self.value_column)
        agg_result = filtered.group_by(self.group_by).agg(agg_expr.alias('agg_value'))

        threshold_condition = ColumnPredicate('agg_value', self.operator, self.threshold)
        passing_groups = agg_result.filter(threshold_condition.evaluate(agg_result))[self.group_by]

        # Return boolean mask for all rows indicating which belong to passing groups / documents
        return df[self.group_by].is_in(passing_groups)


# Convenience functions for creating predicates
def field(name: str, operator: Operator = 'eq') -> ColumnPredicate:
    """Create a predicate for the field column"""
    return ColumnPredicate('field', operator, name)

def annotation(name: str, operator: Operator = 'eq') -> ColumnPredicate:
    """Documents of a specific type"""
    return ColumnPredicate('type', operator, name)

def view(name: str, operator: Operator = 'eq') -> ColumnPredicate:
    """Documents from a specific view"""
    return ColumnPredicate('view', operator, name)

def value(val: Any, operator: Operator = 'eq') -> ColumnPredicate:
    """Create a predicate for the value column"""
    return ColumnPredicate('value', operator, val)

# additional convenience methods for value predicates
def eq(val: Any) -> ColumnPredicate:
    return ColumnPredicate('value', 'eq', val)

def neq(val: Any) -> ColumnPredicate:
    return ColumnPredicate('value', 'ne', val)

def lt(val: Any) -> ColumnPredicate:
    return ColumnPredicate('value', 'lt', val)

def le(val: Any) -> ColumnPredicate:
    return ColumnPredicate('value', 'le', val)

def gt(val: Any) -> ColumnPredicate:
    return ColumnPredicate('value', 'gt', val)

def ge(val: Any) -> ColumnPredicate:
    return ColumnPredicate('value', 'ge', val)

def contains(val: str) -> ColumnPredicate:
    return ColumnPredicate('value', 'contains', val)

def startswith(val: str) -> ColumnPredicate:
    return ColumnPredicate('value', 'startswith', val)

def endswith(val: str) -> ColumnPredicate:
    return ColumnPredicate('value', 'endswith', val)

def in_list(vals: list[Any]) -> ColumnPredicate:
    return ColumnPredicate('value', 'in', vals)

def not_in_list(vals: list[Any]) -> ColumnPredicate:
    return ColumnPredicate('value', 'not_in', vals)

def is_null() -> ColumnPredicate:
    return ColumnPredicate('value', 'is_null', None)

def is_not_null() -> ColumnPredicate:
    return ColumnPredicate('value', 'is_not_null', None)

def custom(func: Callable) -> ColumnPredicate:
    return ColumnPredicate('value', 'custom', func)




# Convenience functions for aggregation predicates
def count(predicate: Predicate, operator: Operator, threshold: Any) -> AggregationPredicate:
    """Filter documents based on count of matching rows"""
    return AggregationPredicate(predicate, 'count', operator, threshold, 'idx')

def sum_filter(predicate: Predicate, operator: Operator, threshold: Any) -> AggregationPredicate:
    """Filter documents based on sum of matching values"""
    return AggregationPredicate(predicate, 'sum', operator, threshold, 'idx', 'value')

def mean_filter(predicate: Predicate, operator: Operator, threshold: Any) -> AggregationPredicate:
    """Filter documents based on mean of matching values"""
    return AggregationPredicate(predicate, 'mean', operator, threshold, 'idx', 'value')

def min_filter(predicate: Predicate, operator: Operator, threshold: Any) -> AggregationPredicate:
    """Filter documents based on minimum of matching values"""
    return AggregationPredicate(predicate, 'min', operator, threshold, 'idx', 'value')

def max_filter(predicate: Predicate, operator: Operator, threshold: Any) -> AggregationPredicate:
    """Filter documents based on maximum of matching values"""
    return AggregationPredicate(predicate, 'max', operator, threshold, 'idx', 'value')

def std_filter(predicate: Predicate, operator: Operator, threshold: Any) -> AggregationPredicate:
    """Filter documents based on standard deviation of matching values"""
    return AggregationPredicate(predicate, 'std', operator, threshold, 'idx', 'value')

def var_filter(predicate: Predicate, operator: Operator, threshold: Any) -> AggregationPredicate:
    """Filter documents based on variance of matching values"""
    return AggregationPredicate(predicate, 'var', operator, threshold, 'idx', 'value')