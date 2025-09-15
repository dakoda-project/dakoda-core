from pathlib import Path

import pytest

from dakoda.corpus import DakodaCorpus
from dakoda.uima import load_dakoda_typesystem, load_cas_from_file

import polars as pl

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
    corpus._document_paths = corpus._document_paths[:10]
    corpus._docs = corpus._docs[:10]
    return corpus

@pytest.fixture
def cas_index():
    return pl.read_csv(TESTFILES_DIR / 'idx_cas.csv')

@pytest.fixture
def empty_corpus():
    return DakodaCorpus(TESTFILES_DIR / "EmptyCorpus")


@pytest.fixture
def sample_index():
    """Create a synthetic index similar to the real data structure"""
    data = [
        (1, 'target_hypothesis', 'POS', 'PosValue', 'NN'),
        (1, 'target_hypothesis', 'POS', 'PosValue', 'ART'),
        (1, 'target_hypothesis', 'POS', 'PosValue', 'VVFIN'),
        (1, 'target_hypothesis', 'Lemma', 'value', 'Mann'),
        (1, 'target_hypothesis', 'Lemma', 'value', 'der'),

        (2, 'learner', 'POS', 'PosValue', 'NN'),
        (2, 'learner', 'POS', 'PosValue', 'NN'),
        (2, 'learner', 'POS', 'PosValue', 'ART'),
        (2, 'learner', 'POS', 'PosValue', 'VVFIN'),
        (2, 'learner', 'Token', 'coveredText', 'Vater'),

        (3, 'target_hypothesis', 'POS', 'PosValue', 'NN'),
        (3, 'target_hypothesis', 'Stage', 'name', 'SVO'),
        (3, 'target_hypothesis', 'Stage', 'name', 'SEP'),
        (3, 'target_hypothesis', 'Stage', 'name', 'SVO'),

        (4, 'learner', 'POS', 'PosValue', 'ART'),
        (4, 'learner', 'POS', 'PosValue', 'PTKNEG'),

        (5, 'target_hypothesis', 'Score', 'value', 10),
        (5, 'target_hypothesis', 'Score', 'value', 20),
        (5, 'target_hypothesis', 'Score', 'value', 30),

        (6, 'learner', 'Score', 'value', 5),
        (6, 'learner', 'Score', 'value', 15),
    ]

    return pl.DataFrame(
        data,
        schema=['idx', 'view', 'type', 'field', 'value'],
        orient='row'
    )

