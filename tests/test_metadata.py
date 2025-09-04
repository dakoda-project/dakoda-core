from dakoda.corpus import DakodaCorpus
from dakoda.metadata import MetaData


def test_meta(test_cas):
    meta = MetaData.from_cas(test_cas)
    assert meta.text.text_tokenCount == 243
    assert (
        meta.corpus.administrative.corpus_admin_acronym == "ComiGs"
    )  # FIXME: This should probably not be correct?


def test_document_meta(test_corpus):
    doc = test_corpus[0]
    meta = test_corpus.document_meta(doc)


def test_document_meta_df(comigs):
    doc = comigs[-1]
    df = comigs.document_meta_df(doc)
    assert not df.is_empty()


def test_corpus(comigs):
    df = comigs.corpus_meta_df
    assert not df.is_empty()
