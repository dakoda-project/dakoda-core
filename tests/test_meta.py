from dakoda.corpus import DakodaCorpus


def test_document_meta(wtld, test_cas):
    meta = wtld.document_meta(test_cas)  # TODO: this should be static
    assert meta.text.text_tokenCount == 243
    assert (
        meta.corpus.administrative.corpus_admin_acronym == "ComiGs"
    )  # FIXME: This should probably not be correct?


def test_document_meta_df(comigs, test_cas):
    df = comigs.document_meta_df(test_cas)
    assert not df.is_empty()


def test_corpus(comigs):
    df = comigs.corpus_meta_df
    assert not df.is_empty()
