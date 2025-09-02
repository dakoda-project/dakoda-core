import io
import random
from pathlib import Path

import polars as pl
from cassis import Cas
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig

from dakoda.dakoda_metadata_scheme import MetaData
from dakoda.dakoda_types import T_META
from dakoda.util import load_cas_from_file, load_dakoda_typesystem
from dakoda.util import traverse_complex


class DakodaCorpus:
    def __init__(self, path):
        self.path = Path(path)
        self.name = self.path.stem
        self.document_paths = [p for p in self.path.glob("*.xmi")]
        self.ts = load_dakoda_typesystem()
        self.json_parser = JsonParser(context=XmlContext(), config=ParserConfig()) # this should be static, I suppose?

    def __repr__(self):
        return f"DakodaCorpus(name={self.name}, path={self.path})"

    def __str__(self):
        return f"Dakoda Corpus: {self.name} at {self.path}"

    def __eq__(self, other):
        if not isinstance(other, DakodaCorpus):
            return False
        return self.name == other.name and self.path == other.path

    def __len__(self):
        return len(self.document_paths)

    def __iter__(self):
        for xmi in self.document_paths:
            yield load_cas_from_file(xmi, self.ts)

    def __getitem__(self, key):
        # TODO: Logical Indexing, list indexing
        if isinstance(key, str) or isinstance(key, Path):
            # TODO: make more robust. Options:
            # path, must be validated. '/some/path/CorpusDir/filename.xmi' --> self.path == key.parent, filename exists
            # string could be filename. 'filename.xmi' --> see if self.path / filename exists
            # string could be id. 'filename' --> see if self.path / filename + xmi exists
            return self._get_by_path(key)
        elif isinstance(key, int):
            return self._get_by_index(key)
        elif isinstance(key, slice):
            return self._get_by_slice(key)
        else:
            raise KeyError(f"Invalid key type: {type(key)}")

    def _get_by_path(self, path: str | Path) -> Cas:
        return load_cas_from_file(self.path / path, self.ts)

    def _get_by_index(self, index: int) -> Cas:
        return self._get_by_path(self.document_paths[index])

    def _get_by_slice(self, indices_slice: slice):
        start, stop, step = indices_slice.indices(len(self))
        return (self._get_by_index(i) for i in range(start, stop, step))

    @property
    def size(self) -> int:
        return len(self)

    @property
    def docs(self):
        return iter(self)

    def random_doc(self) -> Cas:
        """Return a random document from the corpus."""
        if not self.document_paths:
            raise ValueError("No documents in the corpus.")

        xmi = random.choice(self.document_paths)
        return self._get_by_path(xmi)

    # TODO: Should be classmethod, potentiall even on MetaData? MetaData.from_cas(doc)
    # this method can remain as a convenience method.
    def document_meta(self, doc: Cas) -> MetaData:
        """Return the metadata of the given document."""
        for meta in doc.select(T_META):
            if meta.get("key") == "structured_metadata":
                metadata_json_string = meta.get("value")
                document = self.json_parser.parse(
                    io.StringIO(metadata_json_string), MetaData
                )
                return document

        raise ValueError("No structured metadata found in the document.")

    # TODO: should be a classmethod / an instance method on MetaData
    # usage: MetaData.from_cas(doc).to_df()
    def document_meta_df(self, doc: Cas) -> pl.DataFrame:
        meta_dict = {}
        meta = self.document_meta(doc)

        for key, value in traverse_complex(meta):
            meta_dict[key] = value

        return pl.DataFrame(meta_dict)

    @property
    def corpus_meta_df(self) -> pl.DataFrame:
        """Return a DataFrame with metadata for the whole corpus."""

        if _is_cached(self):
            return _read_meta_cache(self)

        data = []
        for doc in self.docs:
            df = self.document_meta_df(doc)
            data.append(df)

        df_all = pl.concat(data, how="vertical")
        _write_meta_cache(self, df_all)
        return df_all


# TODO: instance method
def _is_cached(corpus: DakodaCorpus) -> bool:
    cache = Path(".meta_cache") / corpus.name
    cache.with_suffix(".csv")
    return cache.is_file()


def _write_meta_cache(corpus: DakodaCorpus, df: pl.DataFrame) -> bool:
    cache_dir = Path(".meta_cache") # TODO: constant, configurable via .env
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache = cache_dir / corpus.name
    df.write_csv(cache)
    return True


def _read_meta_cache(corpus: DakodaCorpus) -> pl.DataFrame:
    cache = Path(".meta_cache") / corpus.name
    return pl.read_csv(cache)
