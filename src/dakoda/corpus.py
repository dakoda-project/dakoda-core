from __future__ import annotations

import random
from abc import ABC, abstractmethod
from collections.abc import Iterable, Callable
from pathlib import Path
from typing import Iterator, Literal, List

import polars as pl
from cassis import Cas

from dakoda.metadata import MetaData
from dakoda.query import Predicate
from dakoda.uima import load_cas_from_file, load_dakoda_typesystem, type_to_fieldname, view_to_name

from dataclasses import dataclass

DataSubset = Literal['cas', 'meta']
DATA_SUBSETS = {'cas', 'meta'}

class DakodaDocument:
    def __init__(
        self, cas: Cas | None, id: str | None = None, corpus: DakodaCorpus | None = None
    ):
        self._cas = cas
        self.id = id
        self.corpus = corpus
        # todo: _meta

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
        cached_file = self.corpus.path / f'{self.id}.json'
        if cached_file.is_file():
            try:
                return MetaData.from_json_file(cached_file)
            except Exception as e:
                pass # todo: log

        meta = MetaData.from_cas(self.cas)
        try:
            with open(cached_file, 'w') as f:
                f.write(meta.to_json())
        except Exception as e:
            pass # todo: log

        return meta


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

        self._search_index: dict[DataSubset, pl.DataFrame | None] = {
            'cas': None,
            'meta': None
        }

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
        if isinstance(key, Predicate):
            return self.__getitem__(self._query(key))
        elif isinstance(key, str) or isinstance(key, Path):
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

    def _build_index(self, source_type: DataSubset | None=None, force_rebuild: bool = False):
        if source_type is None:
            self._build_index('cas')
            self._build_index('meta')
            return

        if self._search_index.get(source_type) is not None and not force_rebuild:
            return

        if source_type == 'cas':
            indexer = CasIndexer()

            cache = IndexCache(self, source_type)
            if cache.is_cached and not force_rebuild:
                self._search_index[source_type] = cache.read()
                return
        elif source_type == 'meta':
            indexer = MetaDataIndexer()
            cache = None
        else:
            raise ValueError('Source Type must be either "cas", "meta" or None.')

        self._search_index[source_type] = indexer.index_corpus(self)
        if cache is not None:
            cache.write(self._search_index[source_type])

    def _get_search_index(self, source_type: DataSubset):
        if source_type in DATA_SUBSETS:
            if self._search_index.get(source_type) is None:
                self._build_index(source_type)
            return self._search_index[source_type]
        else:
            raise ValueError('Source Type must be either "cas", "meta" or None.')

    def _query(self, q: Predicate, subset: DataSubset | None = None) -> List[int]:
        if subset in DATA_SUBSETS:
            idx = self._get_search_index(subset)
            return  q.documents(idx).to_list()
        elif subset is None:
            result: set[int] = set()
            for subset in DATA_SUBSETS:
                result.update(self._query(q, subset))
            return list(result)
        else:
            raise ValueError('Subset must be either "cas", "meta" or None.')

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

    def to_entries(self, doc: DakodaDocument, idx = None):
        entries = []
        for key, value in doc.meta.iter_flat():
            entries.append({
                self.column_mapping.get('idx'): idx,
                self.column_mapping.get('view'): None,
                self.column_mapping.get('type'): None,
                self.column_mapping.get('field'): key,
                self.column_mapping.get('value'): value,
            })
        return entries


class IndexCache:
    def __init__(self, corpus: DakodaCorpus, cache_name: DataSubset, cache_dir: str | Path | None = None):
        self.corpus = corpus
        self.cache_name = cache_name
        if cache_dir is None:
            cache_dir = self.corpus.path / ".index"
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    @property
    def cache_file(self):
        return (self.cache_dir / self.cache_name).with_suffix(".parquet")

    @property
    def is_cached(self) -> bool:
        return self.cache_file.is_file()

    def write(self, df: pl.DataFrame) -> bool:
        df.write_parquet(self.cache_file)
        return True

    def read(self) -> pl.DataFrame:
        return pl.read_parquet(self.cache_file)
