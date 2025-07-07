import pytest
import itertools
from dakoda_fixtures import *
from dakoda.corpus import DakodaCorpus

def test_load_corpus():
    wtld = DakodaCorpus("data/WTLD")
    assert wtld.name == "WTLD"

def test_files():
    # TODO use fixture
    wtld = DakodaCorpus("data/ComiGs")
    docs = wtld.documents
    assert len(docs) == 70
    for doc in docs:
        assert doc.suffix == ".xmi"
        assert doc.is_file()

def test_docs():
    # TODO use fixture
    wtld = DakodaCorpus("data/ComiGs")
    assert sum(1 for i in itertools.islice(wtld.docs(), 5)) == 5

# as this will return a different document from the corpus every time the test is called
# it introduces an implicit check for no document in the test corpus having document size == 0
def test_random_doc(test_corpus):
    cas = test_corpus.random_doc()
    assert len(cas.sofa_string) > 0