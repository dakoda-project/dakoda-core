from __future__ import annotations

import random
from pathlib import Path
from typing import Iterator
from collections.abc import Iterable

import polars as pl
from cassis import Cas

from dakoda.metadata import MetaData
from dakoda.uima import load_cas_from_file, load_dakoda_typesystem


class DakodaDocument:
    def __init__(
        self, cas: Cas | None, id: str | None = None, corpus: DakodaCorpus | None = None
    ):
        self._cas = cas
        self.id = id
        self.corpus = corpus

        if corpus is None and cas is None:
            raise ValueError("Cas and Corpus cannot be None.")

    @property
    def text(self) -> str:
        return self.cas.sofa_string

    @property
    def cas(self) -> Cas:
        if self._cas is None:
            cas = load_cas_from_file(self.corpus.path / f'{self.id}.xmi', ts=self.corpus.ts)
            self._cas = cas

        return self._cas


    @property
    def meta(self) -> MetaData:
        cached_file = self.corpus.path / '.meta_cache' / f'{self.id}.json' # todo: encode this information in corpus?
        if cached_file.is_file():
            return MetaData.from_json_file(cached_file)

        return MetaData.from_cas(self.cas)


class DakodaCorpus:
    # this method can remain as a convenience method.
    @staticmethod
    def document_meta(doc: DakodaDocument) -> MetaData:
        """Return the metadata of the given document."""
        return doc.meta

    @staticmethod
    def document_meta_df(doc: DakodaDocument) -> pl.DataFrame:
        return doc.meta.to_df()

    ts = load_dakoda_typesystem()

    def __init__(self, path, cache: CorpusMetaCache | None = None):
        self.path = Path(path)
        self.name = self.path.stem
        self.document_paths = list(self.path.glob("*.xmi"))
        self.document_paths.sort()
        if cache is None:
            cache = CorpusMetaCache(self)
        self._cache = cache
        self._cache.corpus = self

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
            yield self[xmi]

    def __getitem__(self, key):
        # TODO: Querying Corpus
        if isinstance(key, str) or isinstance(key, Path):
            return self._get_by_path(key)
        elif isinstance(key, int):
            return self._get_by_index(key)
        elif isinstance(key, slice):
            return self._get_by_slice(key)
        elif isinstance(key, Iterable):
            return (self.__getitem__(k) for k in key)
        else:
            raise KeyError(f"Invalid key type: {type(key)}")

    def _get_by_path(self, path: str | Path) -> DakodaDocument:
        path = Path(path)
        expected_file = self.path / f'{path.stem}.xmi'

        # todo: probably best to move to DakodaDocument constructor
        if (not path.is_file() and path.suffix == '.xmi') and not expected_file.is_file():
            raise FileNotFoundError(f"No corresponding XMI file for : {path}")

        return DakodaDocument(cas=None, id=path.stem, corpus=self)

    def _get_by_index(self, index: int) -> DakodaDocument:
        return self._get_by_path(self.document_paths[index])

    def _get_by_slice(self, indices_slice: slice) -> Iterator[DakodaDocument]:
        start, stop, step = indices_slice.indices(len(self))
        return (self._get_by_index(i) for i in range(start, stop, step))

    @property
    def size(self) -> int:
        return len(self)

    @property
    def docs(self):
        return iter(self)

    def random_doc(self) -> DakodaDocument:
        """Return a random document from the corpus."""
        if not self.document_paths:
            raise ValueError("No documents in the corpus.")

        xmi = random.choice(self.document_paths)
        return self._get_by_path(xmi)

    def generate_corpus_meta_df(self, use_cached=True) -> pl.DataFrame:
        """Return a DataFrame with metadata for the whole corpus."""

        if use_cached and self._cache.is_empty():
            try:
                return self._cache.read()
            except Exception:
                pass  # fallback to uncached path

        # fixme: there would be a cleaner way using to_dict, but that gives errors, due to the enums used. enum values?
        # fixme: there is no id given for each doc, makes filtering reliant on order of documents
        data = [doc.meta.to_df() for doc in self.docs]

        df_all = pl.concat(data, how="vertical")
        self._cache.write(df_all)
        return df_all


# TODO: cache_dir constant, configurable via .env / config.py?
class CorpusMetaCache:
    def __init__(self, corpus: DakodaCorpus, cache_dir: str | Path = ".meta_cache"):
        self.corpus = corpus
        self.cache_dir = Path(cache_dir)

    # todo: might need a rework with filtered views and subsets and whatnot. probably hashing the document paths is a good idea
    @property
    def cache_file(self):
        return (self.cache_dir / self.corpus.name).with_suffix(".csv")

    def is_empty(self) -> bool:
        return self.cache_file.exists()

    def write(self, df: pl.DataFrame) -> bool:
        cache_dir = self.cache_dir
        cache_dir.mkdir(parents=True, exist_ok=True)
        df.write_csv(self.cache_file)
        return True

    def read(self) -> pl.DataFrame:
        return pl.read_csv(self.cache_file)

    def clear(self):
        self.cache_file.unlink(missing_ok=True)
