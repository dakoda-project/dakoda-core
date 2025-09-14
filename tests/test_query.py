from dakoda.query import field, value, view, annotation, count, mean_filter, eq
import polars as pl


def test_query(cas_index):
    q = annotation('POS') & value('VVFIN')
    result = q.documents(cas_index)

    assert len(cas_index) > q.evaluate(cas_index).sum() > 0
    assert result.dtype == pl.Int64

def test_query_composition(cas_index):
    q = annotation('POS') & value('VVFIN')
    p = annotation('POS') & value('ART')

    # more general queries should return more values
    result = (p | q).evaluate(cas_index)
    result_q = q.evaluate(cas_index)
    assert result_q.sum() < result.sum()

    # nested queries
    result_nested = (annotation('POS') & (value('VVFIN') | value('ART'))).evaluate(cas_index)
    assert all(result == result_nested)

    result_nested_preds = (annotation('POS') & (value('VVFIN') | value('ART'))).evaluate(cas_index)
    assert all(result == result_nested_preds)

def test_numeric_queries(sample_index):
    q = value(5, 'gt')
    rows = q.evaluate(sample_index)
    docs = q.documents(sample_index)
    assert rows.sum() == 4 # 4 VALUES that meet the condition.
    assert docs.count() == 2 # 2 DOCUMENTS that meet the condition.
    assert all(docs == pl.Series([5, 6])) # Document 5 and 6 meet criterion
    assert value(5, 'ge').evaluate(sample_index).sum() == 5

    assert value(15, 'le').evaluate(sample_index).sum() == 3
    assert value(10, 'lt').evaluate(sample_index).sum() == 1
    assert all(value(10, 'lt').documents(sample_index) == pl.Series([6]))

def test_aggregation(sample_index):
    q = count(annotation('POS'), 'ge', 3) # documents with 3 or more POS annotations

    rows = q.evaluate(sample_index)
    doc_ids = q.documents(sample_index)

    # todo: discuss if this is intended behaviour.
    assert rows.sum() == 10 # ALL rows of the document are marked as True, not just matching ones.
    assert doc_ids.count() == 2
    assert all(doc_ids == pl.Series([1, 2]))

    # documents with a mean score of 20 or higher
    doc_ids = mean_filter(annotation('Score'), 'ge', 15).documents(sample_index)
    assert doc_ids.count() == 1
    assert all(doc_ids == pl.Series([5]))

def test_syntactic_sugar(cas_index):
    q = annotation('POS') & eq('VVFIN')
    p = annotation('POS') & value('VVFIN', 'eq')
    assert all(q.evaluate(cas_index) == p.evaluate(cas_index))