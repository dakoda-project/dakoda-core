import shutil
from pathlib import Path

import pytest

from dakoda.corpus import DakodaCorpus

import polars as pl

TESTFILES_DIR = Path(__file__).parent.parent / "data"
TEST_CORPUS_DIR = TESTFILES_DIR / "Merlin_test"

@pytest.fixture
def test_corpus():
    corpus = DakodaCorpus(TEST_CORPUS_DIR)
    return corpus

@pytest.fixture
def test_cas(test_corpus):
    return test_corpus[0].cas


@pytest.fixture
def cas_index():
    return pl.read_csv(TEST_CORPUS_DIR / "cas_idx.csv")


@pytest.fixture
def empty_corpus():
    return DakodaCorpus(TESTFILES_DIR / "EmptyCorpus")


@pytest.fixture
def sample_index():
    """Create a synthetic index similar to the real data structure"""
    data = [
        (1, "target_hypothesis", "POS", "PosValue", "NN"),
        (1, "target_hypothesis", "POS", "PosValue", "ART"),
        (1, "target_hypothesis", "POS", "PosValue", "VVFIN"),
        (1, "target_hypothesis", "Lemma", "value", "Mann"),
        (1, "target_hypothesis", "Lemma", "value", "der"),
        (2, "learner", "POS", "PosValue", "NN"),
        (2, "learner", "POS", "PosValue", "NN"),
        (2, "learner", "POS", "PosValue", "ART"),
        (2, "learner", "POS", "PosValue", "VVFIN"),
        (2, "learner", "Token", "coveredText", "Vater"),
        (3, "target_hypothesis", "POS", "PosValue", "NN"),
        (3, "target_hypothesis", "Stage", "name", "SVO"),
        (3, "target_hypothesis", "Stage", "name", "SEP"),
        (3, "target_hypothesis", "Stage", "name", "SVO"),
        (4, "learner", "POS", "PosValue", "ART"),
        (4, "learner", "POS", "PosValue", "PTKNEG"),
        (5, "target_hypothesis", "Score", "value", 10),
        (5, "target_hypothesis", "Score", "value", 20),
        (5, "target_hypothesis", "Score", "value", 30),
        (6, "learner", "Score", "value", 5),
        (6, "learner", "Score", "value", 15),
    ]

    return pl.DataFrame(
        data, schema=["idx", "view", "type", "field", "value"], orient="row"
    )

def pytest_sessionfinish(session, exitstatus):
    for meta_json in TEST_CORPUS_DIR.glob("*.json"):
        meta_json.unlink()

    index_dir = (TEST_CORPUS_DIR / '.index')
    for index_file in index_dir.glob('*'):
        index_file.unlink()

    if index_dir.exists():
        index_dir.rmdir()

