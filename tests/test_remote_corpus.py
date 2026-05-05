import pytest
from unittest.mock import patch, MagicMock
import zipfile
import io

from dakoda.corpus import DakodaCorpus, DakodaCorpusName


# =========================================================
# Fake ZIP für Remote
# =========================================================
def create_fake_zip_bytes():
    buffer = io.BytesIO()

    with zipfile.ZipFile(buffer, "w") as z:
        z.writestr("doc0.xmi", "<xmi>0</xmi>")
        z.writestr("doc1.xmi", "<xmi>1</xmi>")

    buffer.seek(0)
    return buffer.read()


# =========================================================
# TEST: Local → empty → external fallback to remote
# =========================================================
@patch("requests.get")
def test_local_empty_then_fallback_to_remote(mock_get):

    mock_response = MagicMock()
    mock_response.content = create_fake_zip_bytes()
    mock_response.raise_for_status = lambda: None
    mock_get.return_value = mock_response

    corpus_path = "DLKE-L2"

    corpus = DakodaCorpus(corpus_path)

    if len(corpus) == 0:
        corpus = DakodaCorpus(DakodaCorpusName.DLKE_L2, remote=True)

    assert mock_get.called, "Remote wurde nicht aufgerufen"

    assert len(corpus) == 2

    ids = [doc.id for doc in corpus]
    assert "doc0" in ids
    assert "doc1" in ids