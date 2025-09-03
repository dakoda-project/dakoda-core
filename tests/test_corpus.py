import itertools
import random

import pytest

from cassis import Cas


def test_load_corpus(wtld):
    assert wtld.name == "WTLD"
    assert len(wtld) > 0


def test_files(wtld):
    docs = wtld.document_paths
    assert len(docs) == len(wtld)
    assert all(doc.is_file() and doc.suffix == ".xmi" for doc in docs)


def test_docs(comigs):
    assert sum(1 for i in itertools.islice(comigs.docs, 5)) == 5


def test_subscript_access(comigs):
    # select by index
    first_doc = comigs[0]
    last_doc = comigs[-1]
    assert isinstance(first_doc, Cas)
    assert isinstance(last_doc, Cas)

    # select by slice
    n_docs = len(comigs)
    i = n_docs // 2
    multiple_docs = list(comigs[i : i + 2])
    assert len(multiple_docs) == 2

    # select by path
    path = random.choice(comigs.document_paths)
    doc = comigs[path]
    assert isinstance(doc, Cas)

    # select by id
    doc = comigs['bThN_2']
    assert isinstance(doc, Cas)

    doc = comigs['bThN_2.xmi']
    assert isinstance(doc, Cas)

    with pytest.raises(FileNotFoundError):
        comigs['doesnotexist.xmi']

# as this will return a different document from the corpus every time the test is called
# it introduces an implicit check for no document in the test corpus having document size == 0
def test_random_doc(wtld, empty_corpus):
    cas = wtld.random_doc()
    assert len(cas.sofa_string) > 0

    with pytest.raises(ValueError):
        empty_corpus.random_doc()
