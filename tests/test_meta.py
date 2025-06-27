import pytest
import io
from dakoda_fixtures import test_cas
from dakoda.dakoda_types import T_META
from dakoda.dakoda_metadata_scheme import Document
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

def test_meta_processing(test_cas):
    parser = JsonParser(context=XmlContext(), config=ParserConfig())

    for meta in test_cas.select(T_META):
        if meta.key == "structured_metadata":
            metadata_json_string = meta.value
            doc = parser.parse(io.StringIO(metadata_json_string), Document)
            print(doc)