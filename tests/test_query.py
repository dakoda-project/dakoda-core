from dakoda.query import field, value, view, annotation
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
