import pytest
from dakoda_fixtures import *

#def test_document_meta(test_corpus, test_cas):
def test_document_meta(test_cas):
    test_corpus = DakodaCorpus("data/WTLD")

    meta = test_corpus.document_meta(test_cas)
    assert meta.text.text_tokenCount == 243
    assert meta.corpus.administrative.corpus_admin_acronym == "ComiGs"

def test_document_meta_df(test_cas):
    test_corpus = DakodaCorpus("data/ComiGs")
    df = test_corpus.document_meta_df(test_cas)
    print(df.head(1))
    print(df.columns)

#def test_corpus(test_corpus):
#@pytest.mark.skip()
def test_corpus():
    test_corpus = DakodaCorpus("data/ComiGs")
    df = test_corpus.corpus_meta_df()
    print(df.head(5))