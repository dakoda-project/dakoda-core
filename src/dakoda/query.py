from __future__ import annotations

import operator
from dataclasses import dataclass, replace
from functools import reduce
from typing import Any, Literal
import polars as pl


@dataclass
class Condition:
    operator: str
    value: Any

    def __repr__(self):
        return f"{self.operator}({self.value!r})"

    def check(self, series: pl.Series) -> pl.Series:
        """Check if the series elements satisfy this condition. Returns a boolean Series."""
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
        elif self.operator == 'lambda':
            # Apply lambda function element-wise
            return series.map_elements(self.value, return_dtype=pl.Boolean)
        else:
            raise ValueError(f"Unknown operator: {self.operator}")

@dataclass
class QueryBuilder:
    field_name: str | None = None
    type_name: str | None = None
    view_name: str | None = None
    data_target: Literal['cas', 'meta'] = 'cas'
    conditions: list | None = None

    def select(self, field_name: str | None = None, type_name: str | None = None, view_name: str | None = None):
        updates = {}
        if field_name is not None:
            updates['field_name'] = field_name
        if type_name is not None:
            updates['type_name'] = type_name
        if view_name is not None:
            updates['view_name'] = view_name

        return replace(self, **updates)

    def value(self,
              eq: Any = None,
              ne: Any = None,
              lt: Any = None,
              le: Any = None,
              gt: Any = None,
              ge: Any = None,
              contains: Any = None,
              startswith: str = None,
              endswith: str = None,
              in_: list = None,
              not_in: list = None,
              is_null: bool = None,
              is_not_null: bool = None,
              lambda_: callable = None) -> QueryBuilder:

        current_conditions = self.conditions or []
        new_conditions = current_conditions.copy()

        if eq is not None:
            new_conditions.append(Condition('eq', eq))
        if ne is not None:
            new_conditions.append(Condition('ne', ne))
        if lt is not None:
            new_conditions.append(Condition('lt', lt))
        if le is not None:
            new_conditions.append(Condition('le', le))
        if gt is not None:
            new_conditions.append(Condition('gt', gt))
        if ge is not None:
            new_conditions.append(Condition('ge', ge))
        if contains is not None:
            new_conditions.append(Condition('contains', contains))
        if startswith is not None:
            new_conditions.append(Condition('startswith', startswith))
        if endswith is not None:
            new_conditions.append(Condition('endswith', endswith))
        if in_ is not None:
            new_conditions.append(Condition('in', in_))
        if not_in is not None:
            new_conditions.append(Condition('not_in', not_in))
        if is_null is not None:
            new_conditions.append(Condition('is_null', None))
        if is_not_null is not None:
            new_conditions.append(Condition('is_not_null', None))
        if lambda_ is not None:
            new_conditions.append(Condition('lambda', lambda_))

        return replace(self, conditions=new_conditions)

    def apply_conditions(self, index: pl.DataFrame) -> pl.Series:
        """Apply all conditions to an index and return a series of document indices"""
        if not self.conditions:
            return index['idx'].unique()

        masks = []
        # todo: might be best to have a wrapper class that does these checks index mapping is needed here
        if self.data_target == 'cas' and self.type_name:
            masks.append(index['type'] == self.type_name)

        if self.data_target == 'cas' and self.view_name:
            masks.append(index['view'] == self.view_name)

        if self.field_name:
            masks.append(index['field'] == self.field_name)

        all_true = pl.repeat(True, n=len(index), dtype=pl.Boolean)
        index = index.filter(reduce(lambda x, y: x & y, masks, all_true))

        all_true = pl.repeat(True, n=len(index), dtype=pl.Boolean)
        mask = reduce(lambda x, y: x & y, (condition.check(index['value']) for condition in self.conditions), all_true)

        return index.filter(mask)['idx'].unique()