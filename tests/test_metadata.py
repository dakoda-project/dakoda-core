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
