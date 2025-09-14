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

AggregationFunction = Literal['count', 'sum', 'mean', 'min', 'max', 'std', 'var']

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

        if self.operator == 'eq':
            return series == self.value
        elif self.operator == 'ne':
            return series != self.value
        elif self.operator == 'lt':
            return series < self.value
        elif self.operator == 'le':
            return series <= self.value
        elif self.operator == 'gt':
            return series > self.value
        elif self.operator == 'ge':
            return series >= self.value
        elif self.operator == 'contains':
            return series.str.contains(str(self.value), literal=True)
        elif self.operator == 'startswith':
            return series.str.starts_with(str(self.value))
        elif self.operator == 'endswith':
            return series.str.ends_with(str(self.value))
        elif self.operator == 'in':
            return series.is_in(self.value)
        elif self.operator == 'not_in':
            return ~series.is_in(self.value)
        elif self.operator == 'is_null':
            return series.is_null()
        elif self.operator == 'is_not_null':
            return series.is_not_null()
        elif self.operator == 'custom':
            return series.map_elements(self.value, return_dtype=pl.Boolean)
        else:
            raise ValueError(f"Unknown operator: {self.operator}")

@dataclass
class ConjunctionPredicate(Predicate):
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
class AndPredicate(ConjunctionPredicate):
    """Combines predicates with AND logic"""

    def __init__(self, predicates: list[Predicate]):
        super().__init__(predicates, 'and')


@dataclass
class OrPredicate(ConjunctionPredicate):
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
            return pl.repeat(False, n=len(df), dtype=pl.Boolean, eager=True)

        # Get the appropriate aggregation expression
        if self.agg_function == 'count':
            agg_expr = pl.len()
        elif self.agg_function == 'sum':
            agg_expr = pl.col(self.value_column).sum()
        elif self.agg_function == 'mean':
            agg_expr = pl.col(self.value_column).mean()
        elif self.agg_function == 'min':
            agg_expr = pl.col(self.value_column).min()
        elif self.agg_function == 'max':
            agg_expr = pl.col(self.value_column).max()
        elif self.agg_function == 'std':
            agg_expr = pl.col(self.value_column).std()
        elif self.agg_function == 'var':
            agg_expr = pl.col(self.value_column).var()
        else:
            raise ValueError(f"Unknown aggregation function: {self.agg_function}")

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