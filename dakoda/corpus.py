import random
import io
from typing import Iterable
from pathlib import Path
from cassis import Cas
from dakoda.dakoda_types import T_META
from dakoda.dakoda_metadata_scheme import Document
from dakoda.util import load_cas_from_file, load_dakoda_typesystem
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig

class DakodaCorpus:
    def __init__(self, path):
        self.path = Path(path)
        self.name = self.path.stem
        self.documents = [p for p in self.path.glob('*.xmi')]
        self.ts = load_dakoda_typesystem()
        self.json_parser = JsonParser(context=XmlContext(), config=ParserConfig())

    def __repr__(self):
        return f"DakodaCorpus(name={self.name}, path={self.path})"

    def __str__(self):
        return f"Dakoda Corpus: {self.name} at {self.path}"

    def __eq__(self, other):
        if not isinstance(other, DakodaCorpus):
            return False
        return self.name == other.name and self.path == other.path

    def size(self) -> int:
        return len(self.documents)

    def docs(self) -> Iterable[Cas]:
        for xmi in self.documents:
            cas = load_cas_from_file(xmi, self.ts)
            yield cas

    def random_doc(self) -> Cas:
        """Return a random document from the corpus."""
        if not self.documents:
            raise ValueError("No documents in the corpus.")
        xmi = random.choice(self.documents)
        return load_cas_from_file(xmi, self.ts)
    
    def meta(self, doc: Cas) -> Document:
        """Return the metadata of the given document."""
        for meta in doc.select(T_META):
            if meta.get('key') == "structured_metadata":
                metadata_json_string = meta.get('value')
                document = self.json_parser.parse(io.StringIO(metadata_json_string), Document)
                return document
        
        raise ValueError("No structured metadata found in the document.")