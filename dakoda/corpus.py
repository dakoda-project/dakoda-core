import random
from typing import Iterable
from pathlib import Path
from cassis import Cas
from dakoda.util import load_cas_from_file, load_dakoda_typesystem

class DakodaCorpus:
    def __init__(self, path):
        self.path = Path(path)
        self.name = self.path.stem
        self.documents = [p for p in self.path.glob('*.xmi')]
        self.ts = load_dakoda_typesystem()

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
    
    # https://xsdata.readthedocs.io/en/v24.4/data_binding/json_parsing/

