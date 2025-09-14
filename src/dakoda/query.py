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


