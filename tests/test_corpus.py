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

    assert doc.learner.sentences[0].span == (0, 69)
    assert len(doc.learner.sentences[0].text) == 69

    pos = doc.learner.pos_tags[0]
    pos_th = doc.target_hypothesis.pos_tags[0]

    assert pos.span == (0, 4) and pos.value == "ART"
    assert pos_th.span == (0, 4) and pos_th.value == "ART"
    assert pos_th == pos

    assert doc.learner.text != doc.target_hypothesis.text
    assert not all(
        pos == pos_th
        for pos, pos_th in zip(doc.learner.pos_tags, doc.target_hypothesis.pos_tags)
    )

    learner = doc.learner
    annos = [
        learner.pos_tags,
        learner.tokens,
        learner.sentences,
        learner.lemmas,
        learner.stages,
    ]
    assert all(len(anno) != 0 for anno in annos)

    assert len(doc.text_diff()) > 0

    assert doc.text_diff("ctok", "ctok") != doc.text_diff()


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
