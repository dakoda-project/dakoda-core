import itertools
import random

import pytest

from dakoda.corpus import DakodaDocument, CasIndexer, MetaDataIndexer


def test_load_corpus(test_corpus):
    assert test_corpus.name == "Merlin_test"
    assert len(test_corpus) > 0


def test_files(test_corpus):
    docs = test_corpus.document_paths
    assert len(docs) == len(test_corpus)
    assert all(doc.is_file() and doc.suffix == ".xmi" for doc in docs)


def test_docs(test_corpus):
    assert sum(1 for i in itertools.islice(test_corpus.docs, 5)) == 5

    assert all(isinstance(doc, DakodaDocument) for doc in itertools.islice(test_corpus, 5))
    assert all(
        isinstance(doc, DakodaDocument) for doc in itertools.islice(test_corpus.docs, 5)
    )


def test_subscript_access(test_corpus):
    # select by index
    first_doc = test_corpus[0]
    last_doc = test_corpus[-1]
    assert isinstance(first_doc, DakodaDocument)
    assert first_doc.id == test_corpus.document_paths[0].stem
    assert first_doc.corpus == test_corpus
    assert isinstance(last_doc, DakodaDocument)

    # select by slice
    n_docs = len(test_corpus)
    i = n_docs // 2
    multiple_docs = list(test_corpus[i : i + 2])
    assert len(multiple_docs) == 2

    # select by path
    path = random.choice(test_corpus.document_paths)
    doc = test_corpus[path]
    assert isinstance(doc, DakodaDocument)

    # select by id
    doc = test_corpus[first_doc.id]
    assert isinstance(doc, DakodaDocument)

    doc = test_corpus[first_doc.id + '.xmi']
    assert isinstance(doc, DakodaDocument)

    with pytest.raises(KeyError):
        test_corpus["doesnotexist.xmi"]

    # select by iterable
    idxs = [0, 3, 8]
    docs = list(test_corpus[idxs])
    assert all(isinstance(doc, DakodaDocument) for doc in docs)


def test_random_doc(test_corpus, empty_corpus):
    doc = test_corpus.random_doc()
    assert len(doc.text) > 0

    with pytest.raises(ValueError):
        empty_corpus.random_doc()


def test_document(test_cas, test_corpus):
    # create with external reference
    doc = DakodaDocument(
        cas=test_cas,
        id="TestDOC_27921",
        corpus=test_corpus,
    )

    # cas only
    doc = DakodaDocument(
        cas=test_cas,
    )
    assert len(doc.text) != 0

    assert doc.learner.sentences[0].span == (0, 113)
    assert len(doc.learner.sentences[0].text) == 113

    pos = doc.learner.pos_tags[0]
    pos_th = doc.target_hypothesis.pos_tags[0]

    assert pos.span == (0, 3) and pos.value == "NE"
    assert pos_th.span == (0, 3) and pos_th.value == "NE"
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
