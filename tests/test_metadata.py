from dakoda.metadata import MetaData
import tempfile
from pathlib import Path

def test_meta(test_cas):
    meta = MetaData.from_cas(test_cas)
    assert meta.text.text_tokenCount == 243
    assert (
        meta.corpus.administrative.corpus_admin_acronym == "ComiGs"
    )


def test_serialization_deserialization_with_tmpfile(test_corpus):
    """Test that MetaData can be serialized to JSON and deserialized back correctly"""
    doc = test_corpus[0]
    meta = doc.meta

    with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as tmp_file:
        tmp_path = Path(tmp_file.name)

        try:
            tmp_file.write(meta.to_json())
            tmp_file.flush()  # Ensure data is written

            deserialized_meta = MetaData.from_json_file(tmp_path)

            assert meta == deserialized_meta

        finally:
            tmp_path.unlink(missing_ok=True)