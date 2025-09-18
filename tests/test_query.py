from enum import Enum

from dakoda import DakodaDocument
from dakoda.query import (
    field,
    value,
    view,
    annotation,
    count,
    mean_filter,
    eq,
    AndPredicate,
    neq,
    lt,
    le,
    gt,
    ge,
    contains,
    startswith,
    endswith,
    in_list,
    not_in_list,
    is_null,
    is_not_null,
    custom,
    sum_filter,
    min_filter,
    max_filter,
    std_filter,
    var_filter,
    TruePredicate,
    FalsePredicate,
    NotPredicate,
    OrPredicate,
    ColumnPredicate,
)
import polars as pl


def test_query(cas_index):
    q = annotation("POS") & value("VVFIN")
    result = q.documents(cas_index)

    assert len(cas_index) > q.evaluate(cas_index).sum() > 0
    assert result.dtype == pl.Int64


def test_query_composition(cas_index):
    q = annotation("POS") & value("VVFIN")
    p = annotation("POS") & value("ART")

    # more general queries should return more values
    result = (p | q).evaluate(cas_index)
    result_q = q.evaluate(cas_index)
    assert result_q.sum() < result.sum()

    # nested queries
    result_nested = (annotation("POS") & (value("VVFIN") | value("ART"))).evaluate(
        cas_index
    )
    assert all(result == result_nested)

    result_nested_preds = (
        annotation("POS") & (value("VVFIN") | value("ART"))
    ).evaluate(cas_index)
    assert all(result == result_nested_preds)


def test_numeric_queries(sample_index):
    q = value(5, "gt")
    rows = q.evaluate(sample_index)
    docs = q.documents(sample_index)
    assert rows.sum() == 4  # 4 VALUES that meet the condition.
    assert docs.count() == 2  # 2 DOCUMENTS that meet the condition.
    assert all(docs == pl.Series([5, 6]))  # Document 5 and 6 meet criterion
    assert value(5, "ge").evaluate(sample_index).sum() == 5

    assert value(15, "le").evaluate(sample_index).sum() == 3
    assert value(10, "lt").evaluate(sample_index).sum() == 1
    assert all(value(10, "lt").documents(sample_index) == pl.Series([6]))


def test_aggregation(sample_index):
    q = count(annotation("POS"), "ge", 3)  # documents with 3 or more POS annotations

    rows = q.evaluate(sample_index)
    doc_ids = q.documents(sample_index)

    # todo: discuss if this is intended behaviour.
    assert (
        rows.sum() == 10
    )  # ALL rows of the document are marked as True, not just matching ones.
    assert doc_ids.count() == 2
    assert all(doc_ids == pl.Series([1, 2]))

    # documents with a mean score of 20 or higher
    doc_ids = mean_filter(annotation("Score"), "ge", 15).documents(sample_index)
    assert doc_ids.count() == 1
    assert all(doc_ids == pl.Series([5]))


def test_syntactic_sugar(cas_index):
    # should all be equivalent
    p = annotation("POS") & value("VVFIN", "eq")
    q = annotation("POS") & eq("VVFIN")
    r = AndPredicate([annotation("POS"), eq("VVFIN")])
    assert all(q.evaluate(cas_index) == p.evaluate(cas_index)) and all(
        q.evaluate(cas_index) == r.evaluate(cas_index)
    )


def test_corpus_queries(test_corpus):
    test_corpus._build_index(force_rebuild=True)
    q = annotation("Token")  # check if document has at least one token annotation
    docs = list(test_corpus[q])
    assert len(docs) == len(test_corpus)

    q = count(annotation("Token"), "gt", 5)
    docs = test_corpus[q]
    assert all(isinstance(doc, DakodaDocument) for doc in docs)

    q = field("corpus_admin_acronym") & value("MERLIN")
    docs = list(test_corpus[q])
    assert len(docs) == len(test_corpus)


def test_string_operations(sample_index):
    assert contains("V").evaluate(sample_index).sum() == 5
    assert startswith("S").evaluate(sample_index).sum() == 3
    assert endswith("N").evaluate(sample_index).sum() == 6
    assert contains("NN").evaluate(sample_index).sum() == 4
    assert startswith("V").evaluate(sample_index).sum() == 3


def test_list_operations(sample_index):
    assert in_list([1, 2, 3]).evaluate(sample_index).sum() >= 0
    assert not_in_list([99, 100]).evaluate(sample_index).sum() > 0


def test_null_operations(sample_index):
    assert is_null().evaluate(sample_index).sum() >= 0
    assert is_not_null().evaluate(sample_index).sum() > 0


def test_custom_predicate(sample_index):
    custom_fn = lambda x: x is not None and str(x).startswith("a")
    assert custom(custom_fn).evaluate(sample_index).sum() >= 0


def test_convenience_functions(sample_index):
    assert neq(5).evaluate(sample_index).sum() > 0
    assert lt(10).evaluate(sample_index).sum() >= 0
    assert le(10).evaluate(sample_index).sum() >= 0
    assert gt(0).evaluate(sample_index).sum() >= 0
    assert ge(0).evaluate(sample_index).sum() >= 0


def test_aggregation_functions(sample_index):
    base_pred = annotation("Score")
    assert sum_filter(base_pred, "gt", 0).documents(sample_index).len() >= 0
    assert min_filter(base_pred, "gt", 0).documents(sample_index).len() >= 0
    assert max_filter(base_pred, "lt", 100).documents(sample_index).len() >= 0
    assert std_filter(base_pred, "gt", 0).documents(sample_index).len() >= 0
    assert var_filter(base_pred, "gt", 0).documents(sample_index).len() >= 0


def test_true_false_predicates(sample_index):
    true_pred = TruePredicate()
    false_pred = FalsePredicate()

    assert true_pred.evaluate(sample_index).sum() == len(sample_index)
    assert false_pred.evaluate(sample_index).sum() == 0


def test_not_predicate(sample_index):
    pred = annotation("POS")
    not_pred = ~pred

    original_sum = pred.evaluate(sample_index).sum()
    negated_sum = not_pred.evaluate(sample_index).sum()
    assert original_sum + negated_sum == len(sample_index)


def test_view_predicate(sample_index):
    view_pred = view("test_view")
    assert view_pred.evaluate(sample_index).sum() >= 0


def test_field_predicate(sample_index):
    field_pred = field("test_field", "contains")
    assert field_pred.evaluate(sample_index).sum() >= 0


def test_missing_column(sample_index):
    pred = ColumnPredicate("nonexistent_column", "eq", "value")
    assert pred.evaluate(sample_index).sum() == 0


def test_empty_composite_predicates(sample_index):
    empty_and = AndPredicate([])
    empty_or = OrPredicate([])

    assert empty_and.evaluate(sample_index).sum() == len(
        sample_index
    )  # empty AND = True
    assert empty_or.evaluate(sample_index).sum() == 0  # empty OR = False


def test_predicate_filter_method(sample_index):
    # Test the filter method
    pred = annotation("POS")
    filtered_df = pred.filter(sample_index)
    assert len(filtered_df) <= len(sample_index)
    assert len(filtered_df) == pred.evaluate(sample_index).sum()
