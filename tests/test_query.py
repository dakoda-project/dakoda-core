from dakoda.query import Condition, QueryBuilder
import polars as pl

def test_numeric_conditions(cas_index):
    series = pl.Series([1, 5, 10, 15, 20, 25])
    n = len(series)

    c_lt = Condition('lt', 15)
    r_lt = c_lt.check(series)
    assert r_lt.sum() > 0  # Should have some matches

    c_le = Condition('le', 15)
    r_le = c_le.check(series)
    assert r_le.sum() > r_lt.sum()
    assert r_le.sum() == r_lt.sum() + 1

    c_gt = Condition('gt', 15)
    r_gt = c_gt.check(series)
    assert r_gt.sum() > 0

    c_ge = Condition('ge', 15)
    r_ge = c_ge.check(series)
    assert r_ge.sum() == r_gt.sum() + 1

    assert r_lt.sum() + r_ge.sum() == n
    assert r_le.sum() + r_gt.sum() == n


def test_equality_conditions(cas_index):
    c1 = Condition('eq', 'VVFIN')
    r1 = c1.check(cas_index['value'])
    assert r1.sum() > 0

    c2 = Condition('ne', 'VVFIN')
    r2 = c2.check(cas_index['value'])

    n = len(cas_index['value'])
    assert r2.sum() > 0 and (n - r2.sum()) == r1.sum()


def test_string_conditions():
    string_series = pl.Series(["temp_001", "TEMP_002", "pressure_003", "Temperature", "temp"])

    c_contains = Condition('contains', 'temp')
    r_contains = c_contains.check(string_series)
    assert r_contains.sum() == 2  # "temp_001" and "temp"

    c_starts = Condition('startswith', 'temp')
    r_starts = c_starts.check(string_series)
    assert r_starts.sum() == 2  # "temp_001" and "temp"

    c_ends = Condition('endswith', '001')
    r_ends = c_ends.check(string_series)
    assert r_ends.sum() == 1  # Only "temp_001"

    c_case = Condition('contains', 'TEMP')
    r_case = c_case.check(string_series)
    assert r_case.sum() == 1


def test_membership_operators():
    series = pl.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    n = len(series)

    c_in = Condition('in', [2, 4, 6, 8])
    r_in = c_in.check(series)
    assert r_in.sum() == 4  # Exactly 4 matches

    c_not_in = Condition('not_in', [2, 4, 6, 8])
    r_not_in = c_not_in.check(series)
    assert r_not_in.sum() == 6  # Remaining 6 values

    assert r_in.sum() + r_not_in.sum() == n


def test_null_conditions():
    series_with_nulls = pl.Series([1, None, 3, None, 5, 6])
    n = len(series_with_nulls)

    c_null = Condition('is_null', None)
    r_null = c_null.check(series_with_nulls)
    assert r_null.sum() == 2  # Two None values

    c_not_null = Condition('is_not_null', None)
    r_not_null = c_not_null.check(series_with_nulls)
    assert r_not_null.sum() == 4  # Four non-None values

    assert r_null.sum() + r_not_null.sum() == n


def test_lambda_conditions():
    series = pl.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    n = len(series)

    c_even = Condition('lambda', lambda x: x % 2 == 0)
    r_even = c_even.check(series)
    assert r_even.sum() == 5

    c_complex = Condition('lambda', lambda x: x > 5 and x < 9)
    r_complex = c_complex.check(series)
    assert r_complex.sum() == 3


def test_query_builder_selection(cas_index):
    pos_select = QueryBuilder().select(field_name='PosValue')

    r_vvfin = pos_select.value(eq='VVFIN').apply_conditions(cas_index)
    assert r_vvfin.count() > 0
    assert pl.Int64 == r_vvfin.dtype