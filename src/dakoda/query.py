"""Query system for filtering and searching Dakoda document collections.

This module provides a predicate-based query system for filtering
documents based on various criteria including field values, annotations,
views, and aggregated statistics. Uses Polars DataFrames for
efficient filtering operations.
"""
from __future__ import annotations

import warnings
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Literal, Callable

import polars as pl
from polars.exceptions import PolarsInefficientMapWarning

# when users use lambdas this warning might be thrown. as users are not supposed to use polars directly, we suppress it.
warnings.filterwarnings("ignore", category=PolarsInefficientMapWarning)

Operator = Literal[
    "eq",
    "ne",
    "lt",
    "le",
    "gt",
    "ge",
    "contains",
    "startswith",
    "endswith",
    "in",
    "not_in",
    "is_null",
    "is_not_null",
    "custom",
]

OPERATOR_FUNCTIONS = {
    "eq": lambda series, value: series == value,
    "ne": lambda series, value: series != value,
    "lt": lambda series, value: series < value,
    "le": lambda series, value: series <= value,
    "gt": lambda series, value: series > value,
    "ge": lambda series, value: series >= value,
    "contains": lambda series, value: series.str.contains(str(value), literal=True),
    "startswith": lambda series, value: series.str.starts_with(str(value)),
    "endswith": lambda series, value: series.str.ends_with(str(value)),
    "in": lambda series, value: series.is_in(value),
    "not_in": lambda series, value: ~series.is_in(value),
    "is_null": lambda series, value: series.is_null(),
    "is_not_null": lambda series, value: series.is_not_null(),
    "custom": lambda series, value: series.map_elements(value, return_dtype=pl.Boolean),
}

numeric_operators = {"lt", "le", "gt", "ge"}

AggregationFunction = Literal["count", "sum", "mean", "min", "max", "std", "var"]

AGGREGATION_FUNCTIONS = {
    "count": lambda value_col: pl.len(),
    "sum": lambda value_col: pl.col(value_col).sum(),
    "mean": lambda value_col: pl.col(value_col).mean(),
    "min": lambda value_col: pl.col(value_col).min(),
    "max": lambda value_col: pl.col(value_col).max(),
    "std": lambda value_col: pl.col(value_col).std(),
    "var": lambda value_col: pl.col(value_col).var(),
}

numeric_aggregations = {"sum", "mean", "min", "max", "std", "var"}


class Predicate(ABC):
    """Abstract base class for document filtering predicates.

    Predicates can be combined and modified using the following operators:
        - ~: negate the predicate.
        - &: compose two predicates, using an AND relation.
        - |: compose two predicates, using an OR relation.

    """

    @abstractmethod
    def evaluate(self, index: pl.DataFrame) -> pl.Series:
        """Evaluate the predicate against an index, represented as a polars DataFrame.

        Args:
            index: DataFrame containing document index data.

        Returns:
            Boolean Series indicating which rows match the predicate.
        """
        pass

    def filter(self, index: pl.DataFrame) -> pl.DataFrame:
        """Filter the index rows based on the predicate.

        Args:
            index: DataFrame to filter.

        Returns:
            Filtered index containing only matching rows.
        """
        mask = self.evaluate(index)
        return index.filter(mask)

    def documents(self, index: pl.DataFrame, idx_col="idx") -> pl.Series:
        """Get unique document indices that match the predicate.

        Args:
            index: DataFrame containing document index data.
            idx_col: Name of the column containing document indices.

        Returns:
            Series of unique document indices that satisfy the predicate.
        """
        filtered = self.filter(index)
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
        string_series = series.map_elements(
            converters[pl.String], return_dtype=pl.String
        )
        return (
            string_series
            if cast_type == pl.String
            else string_series.cast(cast_type, strict=False)
        )


@dataclass
class ColumnPredicate(Predicate):
    """Predicate that evaluates a condition against a specific column.

    Tries to safely convert the target column into a datatype that matches the comparison value.

    Args:
        column: Name of the column to evaluate.
        operator: Comparison operator to use.
        value: Value to compare against.
    """
    column: str
    operator: Operator
    value: Any

    def evaluate(self, index: pl.DataFrame) -> pl.Series:
        if self.column not in index.columns:
            return FalsePredicate().evaluate(index)

        series = index[self.column]
        op_fn = OPERATOR_FUNCTIONS[self.operator]

        cast_type = _infer_cast_type(self.value)
        if cast_type is not None:
            series = _cast_safe(series, cast_type)

        if self.operator not in ["is_null", "is_not_null"]:
            return index.select(
                pl.when(series.is_not_null())
                .then(op_fn(series, self.value))
                .otherwise(False)
            ).to_series()
        else:
            return op_fn(series, self.value)


@dataclass
class CompositePredicate(Predicate):
    """Predicate that combines multiple predicates with AND/OR logic.

    Args:
        predicates: List of predicates to combine.
        conjunction_type: Either "and" or "or" for logical combination.
    """
    predicates: list[Predicate]
    conjunction_type: Literal["and", "or"] = "and"

    def __post_init__(self):
        if self.conjunction_type not in ["and", "or"]:
            self.conjunction_type = "and"

    def evaluate(self, index: pl.DataFrame) -> pl.Series:
        if not self.predicates:
            val = True if self.conjunction_type == "and" else False
            return pl.repeat(val, n=len(index), dtype=pl.Boolean, eager=True)

        result = self.predicates[0].evaluate(index)
        for pred in self.predicates[1:]:
            if self.conjunction_type == "and":
                result = result & pred.evaluate(index)
            else:
                result = result | pred.evaluate(index)
        return result


@dataclass
class AndPredicate(CompositePredicate):
    """Combines predicates with AND logic"""

    def __init__(self, predicates: list[Predicate]):
        super().__init__(predicates, "and")


@dataclass
class OrPredicate(CompositePredicate):
    """Combines predicates with OR logic"""

    def __init__(self, predicates: list[Predicate]):
        super().__init__(predicates, "or")


@dataclass
class NotPredicate(Predicate):
    """Negates a predicate"""

    predicate: Predicate

    def evaluate(self, df: pl.DataFrame) -> pl.Series:
        return ~self.predicate.evaluate(df)


@dataclass
class AggregationPredicate(Predicate):
    """Predicate that filters documents based on aggregated statistics.

    First applies a base predicate to filter rows, then aggregates values
    by document and applies a threshold condition to the aggregated results.

    Args:
        base_predicate: Initial predicate to filter rows.
        agg_function: Aggregation function to apply.
        operator: Comparison operator for threshold.
        threshold: Threshold value for comparison.
        group_by: Column to group by for aggregation.
        value_column: Column containing values to aggregate.
    """
    base_predicate: Predicate
    agg_function: AggregationFunction
    operator: Operator
    threshold: Any
    group_by: str = "idx"
    value_column: str = "value"

    def evaluate(self, df: pl.DataFrame) -> pl.Series:
        # First filter by base predicate
        filtered = self.base_predicate.filter(df)

        if len(filtered) == 0:
            return FalsePredicate().evaluate(df)

        if self.agg_function not in AGGREGATION_FUNCTIONS:
            raise ValueError(f"Unknown aggregation function: {self.agg_function}")

        if self.agg_function in numeric_aggregations:
            filtered = filtered.with_columns(
                pl.col(self.value_column).cast(pl.Float64, strict=False)
            )

        agg_expr = AGGREGATION_FUNCTIONS[self.agg_function](self.value_column)
        agg_result = filtered.group_by(self.group_by).agg(agg_expr.alias("agg_value"))

        threshold_condition = ColumnPredicate(
            "agg_value", self.operator, self.threshold
        )
        passing_groups = agg_result.filter(threshold_condition.evaluate(agg_result))[
            self.group_by
        ]

        # Return boolean mask for all rows indicating which belong to passing groups / documents
        return df[self.group_by].is_in(passing_groups.to_list())


# Convenience functions for creating predicates
def field(name: str, operator: Operator = "eq") -> ColumnPredicate:
    """Filter documents containing specific metadata fields.

    Matches documents that have the specified field name in their metadata.
    The operator is applied to the given field name, NOT the values.
    To filter documents with specific values in a particular field, combine field with a value query.

    Args:
        name: Field name to search for.
        operator: How to match the field name (default: exact match).

    Returns:
        Predicate that matches documents with the specified field.

    Examples:
        >>> field("corpus_admin_name")  # Documents that contain 'corpus_admin_name' field
        >>> field("corpus_", "startswith")  # Documents that have fields starting with "corpus_"
        >>> field("corpus_admin_name") & eq("SWIKO") # Documents in which the "corpus_admin_name" field equals "SWIKO"
    """
    return ColumnPredicate("field", operator, name)


def annotation(name: str, operator: Operator = "eq") -> ColumnPredicate:
    """Filter documents containing specific annotation types.

    Matches documents that have the specified annotation type in their CAS data.

    The operator is applied to the annotation type name, NOT the annotation values.
    To filter documents with specific values in particular annotations, combine annotation with a value query.

    Also note, that only checking for an annotation and the corresponding value will check all views by default.
    If you want to examine only the learner's text, combine the query with a view query.

    Args:
        name: Annotation type name to match.
        operator: How to match the annotation type (default: exact match).

    Returns:
        Predicate that matches documents with the specified annotation type.

    Examples:
        >>> annotation("Token")  # Documents that contain Token annotations
        >>> annotation("Stage", "contains")  # Documents with annotation types that have a type name containing "Entity"
        >>> annotation("Stage") & eq("SVO")  # Documents that contain a Stage=SVO annotation
    """
    return ColumnPredicate("type", operator, name)


def view(name: str, operator: Operator = "eq") -> ColumnPredicate:
    """Filter documents from specific document views.

    Matches documents that have data from the specified view perspective.
    The operator is applied to the view name, NOT the view content.
    To filter documents with specific content in a particular view, combine view with a value query.

    Args:
        name: View name to match.
        operator: How to match the view name (default: exact match).

    Returns:
        Predicate that matches documents from the specified view.

    Examples:
        >>> view("learner")  # Documents that have data from learner view
        >>> view("target_hypothesis") # Documents that have an attached target_hypothesis
        >>> view("learner") & contains("mistake")  # Documents from the learner view in which ANY ANNOTATION contains "mistake" as their value
        >>> view("learner") & annotation("Sentence") & (contains("mistake") | contains("error")) # Documents from the learner view in which a sentence contains the words "mistake" or "error"
    """
    return ColumnPredicate("view", operator, name)


def value(val: Any, operator: Operator = "eq") -> ColumnPredicate:
    """Filter documents by values.

    Matches documents where ANY value meets the specified condition.
    This searches across all values in the document index, including metadata values,
    annotation text, and other extracted content.

    Usually you want to combine this with field, annotation and view queries to only check specific variables in the corpus.

    Args:
        val: Value to compare against.
        operator: How to compare the value (default: exact match).

    Returns:
        Predicate that matches documents with the specified value condition.

    Examples:
        >>> value("english")  # Documents containing the value "english" anywhere
        >>> value(0.95, "gt")  # Documents with any numeric values > 0.95
        >>> value("error", "contains")  # Documents with values containing "error"
    """
    return ColumnPredicate("value", operator, val)


# additional convenience methods for value predicates
def eq(val: Any) -> ColumnPredicate:
    """Filter documents containing the given value.

    Matches documents where any indexed field contains exactly the specified value.
    This is equivalent to value(val, "eq") but more concise for exact matching.

    Args:
        val: Exact value to find.

    Returns:
        Predicate for exact value matching.

    Examples:
        >>> eq("German")  # Documents containing "German" in ANY field or annotation
        >>> eq(42)  # Documents with the numeric value 42
        >>> eq(True)  # Documents with boolean value True
    """
    return ColumnPredicate("value", "eq", val)


def neq(val: Any) -> ColumnPredicate:
    """Filter documents excluding specific values.

    Matches documents where indexed fields do NOT contain the specified value.
    This is equivalent to value(val, "ne") but more concise for exclusion.

    Args:
        val: Value to exclude from results.

    Returns:
        Predicate that excludes the specified value.

    Examples:
        >>> neq("incomplete")  # Documents not containing "incomplete"
        >>> neq(0)  # Documents without zero values
        >>> neq(None)  # Documents without null values
    """
    return ColumnPredicate("value", "ne", val)


def lt(val: Any) -> ColumnPredicate:
    """Filter documents with values below a threshold.

    Matches documents where any numeric value is strictly less than the threshold.
    Non-numeric values are ignored. This is equivalent to value(val, "lt").

    Args:
        val: Upper threshold (exclusive).

    Returns:
        Predicate for values below the threshold.

    Examples:
        >>> lt(0.5)  # Documents with any values below 0.5
        >>> lt(100)  # Documents with any counts under 100
        >>> lt(-1)  # Documents with negative values below -1
    """
    return ColumnPredicate("value", "lt", val)


def le(val: Any) -> ColumnPredicate:
    """Filter documents with values at or below a threshold.

    Matches documents where any numeric value is less than or equal to the threshold.
    Non-numeric values are ignored. This is equivalent to value(val, "le").

    Args:
        val: Upper threshold (inclusive).

    Returns:
        Predicate for values at or below the threshold.

    Examples:
        >>> le(1.0)  # Documents with any values up to 1.0
        >>> le(50)  # Documents with any counts of 50 or fewer
        >>> le(0)  # Documents with non-positive values
    """
    return ColumnPredicate("value", "le", val)


def gt(val: Any) -> ColumnPredicate:
    """Filter documents with values above a threshold.

    Matches documents where any numeric value is strictly greater than the threshold.
    Non-numeric values are ignored. This is equivalent to value(val, "gt").

    Args:
        val: Lower threshold (exclusive).

    Returns:
        Predicate for values above the threshold.

    Examples:
        >>> gt(0.8)  # Documents with any values above 0.8
        >>> gt(1000)  # Documents with any counts over 1000
        >>> gt(0)  # Documents with positive values
    """
    return ColumnPredicate("value", "gt", val)


def ge(val: Any) -> ColumnPredicate:
    """Filter documents with values at or above a threshold.

    Matches documents where any numeric value is greater than or equal to the threshold.
    Non-numeric values are ignored. This is equivalent to value(val, "ge").

    Args:
        val: Lower threshold (inclusive).

    Returns:
        Predicate for values at or above the threshold.

    Examples:
        >>> ge(0.9)  # Documents with any values of 0.9 or higher
        >>> ge(10)  # Documents with any counts of at least 10
        >>> ge(0)  # Documents with non-negative values
    """
    return ColumnPredicate("value", "ge", val)


def contains(val: str) -> ColumnPredicate:
    """Filter documents containing specific text substrings.

    Matches documents where any text value contains the specified substring.
    Uses case-sensitive literal substring matching, not regex patterns.
    This is equivalent to value(val, "contains").

    Args:
        val: Text substring to search for.

    Returns:
        Predicate for substring matching.

    Examples:
        >>> contains("error")  # Documents with "error" in any text field
        >>> contains("German")  # Documents mentioning "German"
        >>> contains("@")  # Documents containing email addresses
    """
    return ColumnPredicate("value", "contains", val)


def startswith(val: str) -> ColumnPredicate:
    """Filter documents with text beginning with specific prefixes.

    Matches documents where any text value starts with the specified prefix.
    Uses case-sensitive prefix matching. This is equivalent to value(val, "startswith").

    Args:
        val: Text prefix to match.

    Returns:
        Predicate for prefix matching.

    Examples:
        >>> startswith("The")  # Documents with text starting with "The"
        >>> startswith("ERROR:")  # Documents with error message prefixes
        >>> startswith("http")  # Documents containing URLs
    """
    return ColumnPredicate("value", "startswith", val)


def endswith(val: str) -> ColumnPredicate:
    """Filter documents with text ending with specific suffixes.

    Matches documents where any text value ends with the specified suffix.
    Uses case-sensitive suffix matching. This is equivalent to value(val, "endswith").

    Args:
        val: Text suffix to match.

    Returns:
        Predicate for suffix matching.

    Examples:
        >>> endswith(".pdf")  # Documents referencing PDF files
        >>> endswith("?")  # Documents with questions
        >>> endswith("ing")  # Documents with words ending in "ing"
    """
    return ColumnPredicate("value", "endswith", val)


def in_list(vals: list[Any]) -> ColumnPredicate:
    """Filter documents matching any value from a specified list.

    Matches documents containing any of the specified values in their indexed fields.
    Efficient for checking membership against a known set of valid options.
    This is equivalent to value(vals, "in").

    Args:
        vals: List of acceptable values to match against.

    Returns:
        Predicate for list membership.

    Examples:
        >>> in_list(["English", "German", "French"])  # Documents in these languages
        >>> in_list([1, 2, 3])  # Documents with these specific numbers
        >>> in_list(["draft", "review"])  # Documents in these states
    """
    return ColumnPredicate("value", "in", vals)


def not_in_list(vals: list[Any]) -> ColumnPredicate:
    """Filter documents excluding any value from a specified list.

    Matches documents that do NOT contain any of the specified values in their indexed fields.
    Useful for excluding multiple unwanted categories or values at once.
    This is equivalent to value(vals, "not_in").

    Args:
        vals: List of values to exclude from results.

    Returns:
        Predicate for list exclusion.

    Examples:
        >>> not_in_list(["draft", "incomplete"])  # Exclude unfinished documents
        >>> not_in_list([0, -1])  # Exclude invalid numeric indicators
        >>> not_in_list(["error", "failed"])  # Exclude problematic documents
    """
    return ColumnPredicate("value", "not_in", vals)


def is_null() -> ColumnPredicate:
    """Filter documents containing null or missing values.

    Matches documents where any indexed field has null/missing values.
    Useful for finding incomplete data or identifying optional fields that are empty.
    This is equivalent to value(None, "is_null").

    Returns:
        Predicate that matches documents with null values.

    Examples:
        >>> field("author") & is_null()  # Documents missing author information
        >>> annotation("Score") & is_null()  # Annotations without scores
        >>> is_null()  # Any documents with any null values
    """
    return ColumnPredicate("value", "is_null", None)


def is_not_null() -> ColumnPredicate:
    """Filter documents with present, non-null values.

    Matches documents where indexed fields have actual values (not null or missing).
    Useful for ensuring data completeness or finding populated fields.
    This is equivalent to value(None, "is_not_null").

    Returns:
        Predicate that matches documents with non-null values.

    Examples:
        >>> field("confidence") & is_not_null()  # Documents with confidence scores
        >>> annotation("Label") & is_not_null()  # Only labeled annotations
        >>> is_not_null()  # Documents with any non-null values
    """
    return ColumnPredicate("value", "is_not_null", None)


def custom(func: Callable) -> ColumnPredicate:
    """Filter documents using a custom function that specifies inclusion criteria.

    Matches documents where any value satisfies the user-defined condition function.
    The function receives each value individually and should return True/False.
    This is equivalent to value(func, "custom").

    Args:
        func: Function that takes a value and returns boolean.

    Returns:
        Predicate with custom filtering logic.

    Examples:
        >>> custom(lambda x: len(str(x)) > 10)  # Values longer than 10 characters
        >>> custom(lambda x: x % 2 == 0)  # Even numeric values
        >>> custom(lambda x: "test" in str(x).lower())  # Case-insensitive contains
    """
    return ColumnPredicate("value", "custom", func)


# Convenience functions for aggregation predicates
def count(
    predicate: Predicate, operator: Operator, threshold: Any
) -> AggregationPredicate:
    """Filter documents by the count of rows matching a condition.

    First applies the base predicate to find matching rows, then counts them per document
    and filters documents based on whether the count meets the threshold condition.
    Useful for finding documents with specific quantities of annotations or metadata.

    Args:
        predicate: Base condition to count matches for.
        operator: How to compare the count against the threshold.
        threshold: Required count value for document inclusion.

    Returns:
        Predicate that filters documents by match count.

    Examples:
        >>> count(annotation("Token"), "gt", 100)  # Documents with more than 100 tokens
        >>> count(field("error"), "eq", 0)  # Documents with no error fields
        >>> count(contains("German"), "ge", 5)  # Documents mentioning "German" at least 5 times
    """
    return AggregationPredicate(predicate, "count", operator, threshold, "idx")


def sum_filter(
    predicate: Predicate, operator: Operator, threshold: Any
) -> AggregationPredicate:
    """Filter documents by the sum of numeric values matching a condition.

    First applies the base predicate to find matching rows, sums their numeric values per document,
    then filters documents based on whether the sum meets the threshold condition.
    Non-numeric values are treated as zero in the sum.

    Args:
        predicate: Base condition to identify values to sum.
        operator: How to compare the sum against the threshold.
        threshold: Required sum value for document inclusion.

    Returns:
        Predicate that filters documents by value sum.

    Examples:
        >>> sum_filter(field("score"), "gt", 10.0)  # Documents with total scores above 10
        >>> sum_filter(annotation("Error"), "eq", 0)  # Documents with no error points
        >>> sum_filter(contains("points"), "ge", 100)  # Documents with at least 100 total points
    """
    return AggregationPredicate(predicate, "sum", operator, threshold, "idx", "value")


def mean_filter(
    predicate: Predicate, operator: Operator, threshold: Any
) -> AggregationPredicate:
    """Filter documents by the average of numeric values matching a condition.

    First applies the base predicate to find matching rows, calculates the mean of their numeric values per document,
    then filters documents based on whether the average meets the threshold condition.
    Non-numeric values are excluded from the average calculation.

    Args:
        predicate: Base condition to identify values to average.
        operator: How to compare the mean against the threshold.
        threshold: Required average value for document inclusion.

    Returns:
        Predicate that filters documents by average value.

    Examples:
        >>> mean_filter(field("confidence"), "gt", 0.8)  # Documents with high average confidence
        >>> mean_filter(annotation("Quality"), "ge", 3.0)  # Documents with good average quality ratings
        >>> mean_filter(contains("score"), "lt", 0.5)  # Documents with low average scores
    """
    return AggregationPredicate(predicate, "mean", operator, threshold, "idx", "value")


def min_filter(
    predicate: Predicate, operator: Operator, threshold: Any
) -> AggregationPredicate:
    """Filter documents by the minimum numeric value among matches.

    First applies the base predicate to find matching rows, finds the minimum numeric value per document,
    then filters documents based on whether the minimum meets the threshold condition.
    Non-numeric values are excluded from minimum calculation.

    Args:
        predicate: Base condition to identify values to check.
        operator: How to compare the minimum against the threshold.
        threshold: Required minimum value for document inclusion.

    Returns:
        Predicate that filters documents by minimum value.

    Examples:
        >>> min_filter(field("score"), "gt", 0.5)  # Documents where all scores are above 0.5
        >>> min_filter(annotation("Rating"), "ge", 2)  # Documents with no ratings below 2
        >>> min_filter(contains("confidence"), "gt", 0.7)  # Documents with all confidence values > 0.7
    """
    return AggregationPredicate(predicate, "min", operator, threshold, "idx", "value")


def max_filter(
    predicate: Predicate, operator: Operator, threshold: Any
) -> AggregationPredicate:
    """Filter documents by the maximum numeric value among matches.

    First applies the base predicate to find matching rows, finds the maximum numeric value per document,
    then filters documents based on whether the maximum meets the threshold condition.
    Non-numeric values are excluded from maximum calculation.

    Args:
        predicate: Base condition to identify values to check.
        operator: How to compare the maximum against the threshold.
        threshold: Required maximum value for document inclusion.

    Returns:
        Predicate that filters documents by maximum value.

    Examples:
        >>> max_filter(field("error_rate"), "lt", 0.1)  # Documents with peak errors under 10%
        >>> max_filter(annotation("Difficulty"), "le", 5)  # Documents with maximum difficulty ≤ 5
        >>> max_filter(contains("temperature"), "gt", 100)  # Documents with temperatures over 100
    """
    return AggregationPredicate(predicate, "max", operator, threshold, "idx", "value")


def std_filter(
    predicate: Predicate, operator: Operator, threshold: Any
) -> AggregationPredicate:
    """Filter documents by the standard deviation of numeric values matching a condition.

    First applies the base predicate to find matching rows, calculates the standard deviation of their numeric values per document,
    then filters documents based on whether the variability meets the threshold condition.
    Non-numeric values are excluded from standard deviation calculation.

    Args:
        predicate: Base condition to identify values to analyze.
        operator: How to compare the standard deviation against the threshold.
        threshold: Required standard deviation for document inclusion.

    Returns:
        Predicate that filters documents by value variability.

    Examples:
        >>> std_filter(field("scores"), "lt", 0.2)  # Documents with consistent scores
        >>> std_filter(annotation("Timing"), "gt", 1.0)  # Documents with variable timing
        >>> std_filter(contains("measurement"), "le", 0.1)  # Documents with low measurement variance
    """
    return AggregationPredicate(predicate, "std", operator, threshold, "idx", "value")


def var_filter(
    predicate: Predicate, operator: Operator, threshold: Any
) -> AggregationPredicate:
    """Filter documents by the variance of numeric values matching a condition.

    First applies the base predicate to find matching rows, calculates the variance of their numeric values per document,
    then filters documents based on whether the spread meets the threshold condition.
    Non-numeric values are excluded from variance calculation.

    Args:
        predicate: Base condition to identify values to analyze.
        operator: How to compare the variance against the threshold.
        threshold: Required variance for document inclusion.

    Returns:
        Predicate that filters documents by value variance.

    Examples:
        >>> var_filter(field("measurements"), "lt", 0.5)  # Documents with low variance data
        >>> var_filter(annotation("Responses"), "gt", 2.0)  # Documents with high variance responses
        >>> var_filter(contains("rating"), "eq", 0)  # Documents with identical ratings (no variance)
    """
    return AggregationPredicate(predicate, "var", operator, threshold, "idx", "value")
