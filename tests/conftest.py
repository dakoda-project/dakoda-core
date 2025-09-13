from pathlib import Path

import pytest

from dakoda.corpus import DakodaCorpus
from dakoda.uima import load_dakoda_typesystem, load_cas_from_file

import polars as pl

# TODO: make configurable via .env file, this should be the default
TESTFILES_DIR = Path(__file__).parent.parent / "data"


@pytest.fixture
def test_cas():
    return load_cas_from_file(TESTFILES_DIR / "test.xmi", load_dakoda_typesystem())


@pytest.fixture
def comigs():
    return DakodaCorpus(TESTFILES_DIR / "ComiGs")


@pytest.fixture
def wtld():
    return DakodaCorpus(TESTFILES_DIR / "WTLD")


@pytest.fixture
def test_corpus():
    corpus = DakodaCorpus(TESTFILES_DIR / "WTLD")
    corpus.document_paths = corpus.document_paths[:10]
    return corpus

@pytest.fixture
def cas_index():
    return pl.read_csv(TESTFILES_DIR / 'idx_cas.csv')

@pytest.fixture
def empty_corpus():
    return DakodaCorpus(TESTFILES_DIR / "EmptyCorpus")
