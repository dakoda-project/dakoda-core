from dakoda.dakoda_metadata_scheme import Document
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

parser_config = ParserConfig()
xml_context = XmlContext()
parser = JsonParser(context=xml_context, config=parser_config)
sample = "WzKL_1.v1.json"

# python object
meta = parser.parse(sample, Document)
print(meta.corpus)