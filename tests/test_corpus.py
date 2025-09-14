import itertools
import random

import pytest

from dakoda.corpus import DakodaDocument, CasIndexer, MetaDataIndexer


def test_load_corpus(wtld):
    assert wtld.name == "WTLD"
    assert len(wtld) > 0


def test_files(wtld):
    docs = wtld.document_paths
    assert len(docs) == len(wtld)
    assert all(doc.is_file() and doc.suffix == ".xmi" for doc in docs)


def test_docs(comigs):
    assert sum(1 for i in itertools.islice(comigs.docs, 5)) == 5

    assert all(isinstance(doc, DakodaDocument) for doc in itertools.islice(comigs, 5))
    assert all(
        isinstance(doc, DakodaDocument) for doc in itertools.islice(comigs.docs, 5)
    )


def test_subscript_access(comigs):
    # select by index
    first_doc = comigs[0]
    last_doc = comigs[-1]
    assert isinstance(first_doc, DakodaDocument)
    assert first_doc.id == "2mVs_1"
    assert first_doc.corpus == comigs
    assert isinstance(last_doc, DakodaDocument)

    # select by slice
    n_docs = len(comigs)
    i = n_docs // 2
    multiple_docs = list(comigs[i : i + 2])
    assert len(multiple_docs) == 2

    # select by path
    path = random.choice(comigs.document_paths)
    doc = comigs[path]
    assert isinstance(doc, DakodaDocument)

    # select by id
    doc = comigs["bThN_2"]
    assert isinstance(doc, DakodaDocument)

    doc = comigs["bThN_2.xmi"]
    assert isinstance(doc, DakodaDocument)

    with pytest.raises(KeyError):
        comigs["doesnotexist.xmi"]

    # select by iterable
    idxs = [0, 3, 8]
    docs = list(comigs[idxs])
    assert all(isinstance(doc, DakodaDocument) for doc in docs)


def test_random_doc(wtld, empty_corpus):
    doc = wtld.random_doc()
    assert len(doc.text) > 0

    with pytest.raises(ValueError):
        empty_corpus.random_doc()


def test_document(test_cas, comigs):
    # create with external reference
    doc = DakodaDocument(
        cas=test_cas,
        id="TestDOC_27921",
        corpus=comigs,
    )

    # cas only
    doc = DakodaDocument(
        cas=test_cas,
    )
    assert len(doc.text) != 0


def test_cas_indexer(test_corpus):
    indexer = CasIndexer()

    doc = test_corpus.random_doc()
    doc_df = indexer.index_document(doc)
    df = indexer.index_corpus(test_corpus)

    assert df.columns == doc_df.columns
    assert all(col in indexer.field_mappings.keys() for col in df.columns)


def test_meta_indexer(test_corpus):
    indexer = MetaDataIndexer()
    doc = test_corpus.random_doc()
    doc_df = indexer.index_document(doc)
    df = indexer.index_corpus(test_corpus)
    assert df.columns == doc_df.columns
    assert all(col in indexer.field_mappings.keys() for col in df.columns)