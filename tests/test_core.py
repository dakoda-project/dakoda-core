import pytest
from dakoda_fixtures import *

def test_basic_access(test_cas):
    assert len(test_cas.sofa_string) == 1184