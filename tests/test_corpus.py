import itertools

import pytest


def test_load_corpus(wtld):
    assert wtld.name == "WTLD"
    assert len(wtld) > 0


def test_files(wtld):
    docs = wtld.documents
    assert len(docs) == len(wtld)
    assert all(doc.is_file() and doc.suffix == ".xmi" for doc in docs)


def test_docs(comigs):
    assert sum(1 for i in itertools.islice(comigs.docs, 5)) == 5


# as this will return a different document from the corpus every time the test is called
# it introduces an implicit check for no document in the test corpus having document size == 0
def test_random_doc(wtld, empty_corpus):
    cas = wtld.random_doc()
    assert len(cas.sofa_string) > 0

    with pytest.raises(ValueError):
        empty_corpus.random_doc()
