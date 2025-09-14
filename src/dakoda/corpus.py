from __future__ import annotations

import random
from abc import ABC, abstractmethod
from collections.abc import Iterable, Callable
from pathlib import Path
from typing import Iterator, Literal

import polars as pl
from cassis import Cas

from dakoda.metadata import MetaData
from dakoda.uima import load_cas_from_file, load_dakoda_typesystem, type_to_fieldname, view_to_name

from dataclasses import dataclass


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
    ts = load_dakoda_typesystem()

    def __init__(self, path):
        self.path = Path(path)
        self.name = self.path.stem
        self._document_paths = list(self.path.glob("*.xmi"))
        self._document_paths.sort()

        self._docs = []
        self._id_to_doc = {}
        for p in self.document_paths:
            doc = DakodaDocument(cas=None, id=p.stem, corpus=self)
            self._docs.append(doc)
            self._id_to_doc[doc.id] = doc


    def __repr__(self):
        return f"DakodaCorpus(name={self.name}, path={self.path})"

    def __str__(self):
        return f"Dakoda Corpus: {self.name} at {self.path}"

    def __eq__(self, other):
        if not isinstance(other, DakodaCorpus):
            return False
        return self.name == other.name and self.path == other.path

    def __len__(self):
        return len(self._docs)

    def __iter__(self):
        return iter(self._docs)

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
        return self._id_to_doc[Path(path).stem]

    def _get_by_index(self, index: int) -> DakodaDocument:
        return self._docs[index]

    def _get_by_slice(self, indices_slice: slice) -> Iterator[DakodaDocument]:
        start, stop, step = indices_slice.indices(len(self))
        return (self._get_by_index(i) for i in range(start, stop, step))

    @property
    def size(self) -> int:
        return len(self)

    @property
    def docs(self):
        return self._docs.copy()

    @property
    def document_paths(self):
        return self._document_paths.copy()

    def random_doc(self) -> DakodaDocument:
        """Return a random document from the corpus."""
        if not self._docs:
            raise ValueError("No documents in the corpus.")
        return random.choice(self._docs)


@dataclass
class FieldMapping:
    name: str
    dtype: any
    mapping_fn: Callable | None = None


class Indexer(ABC):
    default_field_mappings = {
        'idx': FieldMapping('idx', pl.Int64),
        'view': FieldMapping('view', pl.Categorical),
        'type': FieldMapping('type', pl.Categorical),
        'field': FieldMapping('field', pl.Categorical),
        'value': FieldMapping('value', pl.Object)
    }

    def __init__(self, field_mappings: dict[str, FieldMapping] | None = None):
        if field_mappings is None:
            field_mappings = self.default_field_mappings.copy()
        self.field_mappings = field_mappings

    @property
    def schema(self):
        return {field_mapping.name: field_mapping.dtype for field_mapping in self.field_mappings.values()}

    @property
    def column_mapping(self):
        return {name: mapping.name for name, mapping in self.field_mappings.items()}

    @abstractmethod
    def to_entries(self, doc: DakodaDocument, idx = None):
        pass

    def index_corpus(self, corpus):
        entries = []
        for i, doc in enumerate(corpus.docs):
            entries.extend(self.to_entries(doc, i))
        return pl.DataFrame(entries, self.schema)

    def index_document(self, doc: DakodaDocument):
        entries = self.to_entries(doc)
        return pl.DataFrame(entries, self.schema)


class CasIndexer(Indexer):
    default_field_mappings = {
        'idx': FieldMapping('idx', pl.Int64),
        'view': FieldMapping('view', pl.Categorical),
        'type': FieldMapping('type', pl.Categorical),
        'field': FieldMapping('field', pl.Categorical),
        'value': FieldMapping('value', pl.Utf8)
    }

    def to_entries(self, doc: DakodaDocument, idx = None):
        entries = []
        cas = doc.cas
        for view_name, cas_view_name in view_to_name.items():
            view = cas.get_view(cas_view_name)
            for type_name, value_name in type_to_fieldname.items():
                annotations = view.select(type_name)
                for annotation in annotations:
                    if value_name == 'coveredText':
                        value = annotation.get_covered_text()
                    else:
                        value = annotation[value_name]
                    entry = {
                        self.column_mapping.get('idx'): idx,
                        self.column_mapping.get('view'): view_name,
                        self.column_mapping.get('type'): type_name.split('.')[-1],
                        self.column_mapping.get('field'): value_name,
                        self.column_mapping.get('value'): value
                    }
                    entries.append(entry)
        return entries


class MetaDataIndexer(Indexer):
    default_field_mappings = {
        'idx': FieldMapping('idx', pl.Int64),
        'field': FieldMapping('field', pl.Categorical),
        'value': FieldMapping('value', pl.Object)
    }

    def to_entries(self, doc: DakodaDocument, idx = None):
        entries = []
        for key, value in doc.meta.iter_flat():
            entries.append({
                self.column_mapping.get('idx'): idx,
                self.column_mapping.get('field'): key,
                self.column_mapping.get('value'): value,
            })
        return entries


# TODO: generalize & test. serialisation and deserialisation needs work. idea: add type column and module column. dynamic imports
class IndexCache:
    def __init__(self, corpus: DakodaCorpus, cache_name: Literal['cas', 'meta'], cache_dir: str | Path | None = None):
        self.corpus = corpus
        self.cache_name = cache_name
        if cache_dir is None:
            cache_dir = self.corpus.path / ".cache"
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    @property
    def cache_file(self):
        return (self.cache_dir / self.cache_name).with_suffix(".parquet")

    def write(self, df: pl.DataFrame) -> bool:
        df.write_parquet(self.cache_file)
        return True

    def read(self) -> pl.DataFrame:
        return pl.read_parquet(self.cache_file)
