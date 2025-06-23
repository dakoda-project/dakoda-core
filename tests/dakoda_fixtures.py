import pytest
from dakoda.corpus import DakodaCorpus
from dakoda.util import load_dakoda_typesystem, load_cas_from_file

@pytest.fixture
def test_cas():
    ts = load_dakoda_typesystem()
    return load_cas_from_file('data/test.xmi', ts)

@pytest.fixture
def test_corpus():
    return DakodaCorpus("data/WTLD")
