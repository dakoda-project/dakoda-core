from dakoda.query import field, value, view, annotation, Query as Q
import polars as pl

def test_query(cas_index):
    q = Q(annotation('POS') & value('VVFIN'))
    result = q.documents(cas_index)

    assert result.count() > 0
    assert result.dtype == pl.Int64