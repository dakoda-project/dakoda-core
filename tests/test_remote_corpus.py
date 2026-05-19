from pathlib import Path
from zipfile import ZipFile
import io

import pytest

from dakoda.corpus import DakodaCorpus, DakodaCorpusName


# =========================================================
# FIXTURES
# =========================================================

@pytest.fixture
def local_corpus_dir(tmp_path: Path) -> Path:
    corpus_dir = tmp_path / "TEST_CORPUS"
    corpus_dir.mkdir()

    (corpus_dir / "doc1.xmi").write_text("<xmi></xmi>")
    (corpus_dir / "doc2.xmi").write_text("<xmi></xmi>")

    return corpus_dir


@pytest.fixture
def fake_remote_zip() -> bytes:
    buffer = io.BytesIO()

    with ZipFile(buffer, "w") as zf:
        zf.writestr("doc1.xmi", "<xmi></xmi>")
        zf.writestr("doc2.xmi", "<xmi></xmi>")

    buffer.seek(0)
    return buffer.read()


# =========================================================
# LOCAL LOADING
# =========================================================

def test_local_corpus_loading(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    assert corpus.remote is False
    assert corpus.name == "TEST_CORPUS"

    assert len(corpus) == 2
    assert corpus.size == 2

    assert corpus.document_paths is not None
    assert len(corpus.document_paths) == 2


def test_local_corpus_invalid_path():

    with pytest.raises(FileNotFoundError):
        DakodaCorpus(Path("does_not_exist"))


# =========================================================
# REMOTE LOADING (ENUM)
# =========================================================

def test_remote_corpus_loading_enum(monkeypatch, tmp_path, fake_remote_zip):

    class FakeResponse:
        status_code = 200
        content = fake_remote_zip

        def raise_for_status(self):
            return None

    monkeypatch.setattr(
        "dakoda.corpus.requests.get",
        lambda *a, **k: FakeResponse(),
    )

    monkeypatch.setattr(
        DakodaCorpus,
        "CACHE_DIR",
        tmp_path / ".dakoda" / "corpora",
    )

    corpus = DakodaCorpus(DakodaCorpusName.DLKE_L2)

    assert corpus.remote is True
    assert corpus.name == "DLKE-L2"
    assert len(corpus) == 2

    cache_path = tmp_path / ".dakoda" / "corpora" / "DLKE-L2"

    assert cache_path.exists()
    assert (cache_path / "doc1.xmi").exists()


# =========================================================
# REMOTE LOADING (STRING)
# =========================================================

def test_remote_corpus_loading_string(monkeypatch, tmp_path, fake_remote_zip):

    class FakeResponse:
        status_code = 200
        content = fake_remote_zip

        def raise_for_status(self):
            return None

    monkeypatch.setattr(
        "dakoda.corpus.requests.get",
        lambda *a, **k: FakeResponse(),
    )

    monkeypatch.setattr(
        DakodaCorpus,
        "CACHE_DIR",
        tmp_path / ".dakoda" / "corpora",
    )

    corpus = DakodaCorpus("DLKE_L2")

    assert corpus.remote is True
    assert corpus.name == "DLKE-L2"
    assert len(corpus) == 2


# =========================================================
# CACHE USAGE (NO DOWNLOAD)
# =========================================================

def test_remote_uses_cache(monkeypatch, tmp_path):

    cache_dir = tmp_path / ".dakoda" / "corpora" / "DLKE-L2"
    cache_dir.mkdir(parents=True)

    (cache_dir / "doc1.xmi").write_text("<xmi></xmi>")
    (cache_dir / "doc2.xmi").write_text("<xmi></xmi>")

    called = False

    def fake_get(*args, **kwargs):
        nonlocal called
        called = True
        raise RuntimeError("Should not download")

    monkeypatch.setattr("dakoda.corpus.requests.get", fake_get)

    monkeypatch.setattr(
        DakodaCorpus,
        "CACHE_DIR",
        tmp_path / ".dakoda" / "corpora",
    )

    corpus = DakodaCorpus("DLKE_L2")

    assert len(corpus) == 2
    assert called is False


# =========================================================
# URL BUILDER
# =========================================================

def test_build_remote_url():

    url = DakodaCorpus._build_remote_url("DLKE-L2")

    assert "DLKE-L2_xmi.zip" in url
    assert "dakoda.org" in url


# =========================================================
# COLLECTION BEHAVIOUR
# =========================================================

def test_len(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    assert len(corpus) == 2
    assert corpus.size == 2


def test_iteration(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    docs = list(corpus)

    assert len(docs) == 2


def test_getitem_index(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    doc = corpus[0]

    assert doc.id == "doc1"


def test_getitem_path(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    doc = corpus["doc1"]

    assert doc.id == "doc1"


def test_getitem_slice(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    docs = corpus[:1]

    assert isinstance(docs, list)
    assert len(docs) == 1


def test_getitem_iterable(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    docs = corpus[[0, 1]]

    assert isinstance(docs, list)
    assert len(docs) == 2


# =========================================================
# EQUALITY
# =========================================================

def test_corpus_equality(local_corpus_dir):

    c1 = DakodaCorpus(local_corpus_dir)
    c2 = DakodaCorpus(local_corpus_dir)

    assert c1 == c2


# =========================================================
# REPR / STR
# =========================================================

def test_repr(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    r = repr(corpus)

    assert "DakodaCorpus" in r
    assert corpus.name in r


def test_str(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    s = str(corpus)

    assert corpus.name in s


# =========================================================
# RANDOM DOC
# =========================================================

def test_random_doc(local_corpus_dir):

    corpus = DakodaCorpus(local_corpus_dir)

    doc = corpus.random_doc()

    assert doc is not None
    assert doc.id in {"doc1", "doc2"}


# =========================================================
# INVALID INPUT
# =========================================================

def test_invalid_constructor_type():

    with pytest.raises(TypeError):
        DakodaCorpus(12345)