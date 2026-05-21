"""Dakoda corpus and document management.

This module provides classes for managing collections of linguistic documents
in the Dakoda format.
"""

from __future__ import annotations

import io
import random
from abc import ABC, abstractmethod
from collections.abc import Iterable, Callable
from pathlib import Path
from typing import Iterator, Literal, List

import difflib

import polars as pl
from cassis import Cas

from dakoda.metadata import MetaData
from dakoda.query import Predicate
from dakoda.uima import (
    load_cas_from_file,
    load_dakoda_typesystem,
    type_to_fieldname,
    view_to_name,
    DocumentView,
)

from dataclasses import dataclass

from enum import Enum
import requests
import zipfile

DataSubset = Literal["cas", "meta"]
DATA_SUBSETS = {"cas", "meta"}

class DakodaDocument:
    """Represents a single document in a Dakoda corpus.

    Provides access to document data, i.e. text, annotations and metadata.

    Args:
        cas: Optional CAS object containing document annotations.
        id: Unique identifier for the document.
        corpus: Parent corpus containing this document.

    Raises:
        ValueError: If both cas and corpus are None.
    """
    def __init__(
        self, cas: Cas | None, id: str | None = None, corpus: DakodaCorpus | None = None
    ):
        self._cas = cas
        self.id = id
        self.corpus = corpus
        self._meta = None

        if corpus is None and cas is None:
            raise ValueError("Cas and Corpus cannot be None.")

    @property
    def text(self) -> str:
        """Get the raw text content of the document, i.e. the text the learner produced.

        Returns:
            The document's text.
        """
        return self.cas.sofa_string

    @property
    def cas(self) -> Cas:
        """Get the CAS object for this document.

        If the CAS is not already loaded, loads it from the corresponding
        XMI file using the corpus typesystem.

        Returns:
            The CAS object containing document annotations.
        """
        if self._cas is None:
            cas = load_cas_from_file(
                self.corpus.path / f"{self.id}.xmi", ts=self.corpus.ts
            )
            self._cas = cas

        return self._cas

    @property
    def meta(self) -> MetaData:
        """Get document metadata with caching support.

        Attempts to load cached metadata from JSON file first, otherwise
        extracts metadata from CAS and caches it for future use.

        Returns:
            MetaData object containing document metadata.
        """
        if self._meta is None:
            cached_file = self.corpus.path / f"{self.id}.json"
            if cached_file.is_file():
                self._meta = MetaData.from_json_file(cached_file)
            else:
                self._meta = MetaData.from_cas(self.cas)
                with open(cached_file, "w") as f:
                    f.write(self._meta.to_json_string())

        return self._meta

    def view(self, view_name):
        view_name = view_to_name.get(view_name, view_name)
        return DocumentView(view_name, self.cas)

    @property
    def learner(self):
        """Get the learner view of the document and all attached annotations.

        Returns:
            DocumentView object for the learner view.
        """
        return self.view(view_to_name["learner"])

    @property
    def target_hypothesis(self):
        """Get the target hypothesis view of the document.

        Returns:
            DocumentView object for the target hypothesis view.
        """
        return self.view(view_to_name["target_hypothesis"])

    def text_diff(self, view_1: str = "learner", view_2: str = "target_hypothesis") -> str:
        """Generate a string representing the difference between texts in different document views.

        Uses a view's tokens to generate the text to compare. If a view has not been tokenized, this will fail.

        Args:
            view_1: Name of the first view to compare.
            view_2: Name of the second view to compare.

        Returns:
            String containing the context diff between the two views.
        """

        view_1 = view_to_name.get(view_1, view_1)
        view_2 = view_to_name.get(view_2, view_2)
        tokens_1 = [token.text for token in self.view(view_1).tokens]
        tokens_2 = [token.text for token in self.view(view_2).tokens]
        return "".join(difflib.context_diff(tokens_1, tokens_2))

class DakodaClosedCorpusName(Enum):
    ASKO_L2 = "ASKO-L2"
    DLKE_L2 = "DLKE-L2"
    DLKÜ_L2 = "DLKÜ-L2"

class DakodaRestrictedCorpusName(Enum):
    AUGS_L2 = "AUGS-L2"
    BELD_L2 = "BELD-L2"
    CDGE_L2 = "CDGE-L2"
    CDPL_L2 = "CDPL-L2"
    DISH_L2 = "DISH-L2"
    DISK_L2 = "DISK-L2"
    DIWT_L2 = "DIWT-L2"
    DUO_L2 = "DUO-L2"
    KLP1_L2 = "KLP1-L2"
    KLP1_LX = "KLP1-Lx"
    KOKO_L1 = "KOKO-L1"
    KOKO_LX = "KOKO-Lx"
    LEON_L1 = "LEON-L1"
    LEON_L2 = "LEON-L2"
    MULT_L1 = "MULT-L1"
    MULT_L2 = "MULT-L2"
    SWIK_L1 = "SWIK-L1"
    SWIK_L2 = "SWIK-L2"
    SWIK_LX = "SWIK-Lx"

class DakodaPublicCorpusName(Enum):
    BMAT_L2 = "BMAT-L2"
    COGS_L2 = "COGS-L2"
    DIGS_L2 = "DIGS-L2"
    FA_ESSA_L2 = "FA-ESSA-L2"
    FA_GBWT_L2 = "FA-GBWT-L2"
    FA_GPPT_L2 = "FA-GPPT-L2"
    FA_KAND_L2 = "FA-KAND-L2"
    FA_KOEX_L2 = "FA-KOEX-L2"
    FA_SUMM_L2 = "FA-SUMM-L2"
    FA_WHIG_L2 = "FA-WHIG-L2"
    MERL_L2 = "MERL-L2"
    OSNA_L1 = "OSNA-L1"
    OSNA_L2 = "OSNA-L2"
    OSNA_LX = "OSNA-Lx"
    PETE_L1 = "PETE-L1"
    PETE_L2 = "PETE-L2"
    RUEG_HL = "RUEG-HL"
    RUEG_L1 = "RUEG-L1"
    RUEG_LX = "RUEG-Lx"

def _merge_enum_values(*enum_classes):
    values = {}
    for enum_class in enum_classes:
        for member in enum_class:
            values[member.name] = member.value
    return Enum("DakodaCorpusName", values)

DakodaCorpusName = _merge_enum_values(
    DakodaPublicCorpusName,
    DakodaRestrictedCorpusName,
    DakodaClosedCorpusName
)

class DakodaCorpus:
    """A collection of Dakoda documents."""

    ts = load_dakoda_typesystem()

    CACHE_DIR = Path.cwd() / ".dakoda" / "corpora"

    def __init__(
        self,
        source: DakodaPublicCorpusName | DakodaCorpusName | str | Path,
    ):

        self.remote = False

        # =====================================================
        # Index-Struktur
        # =====================================================
        self._search_index: dict[DataSubset, pl.DataFrame | None] = {
            "cas": None,
            "meta": None,
        }

        # =====================================================
        # Lokal über Path
        # =====================================================
        if isinstance(source, Path):
            self.path = source
            self.name = source.stem
            self._init_from_filesystem(source)
        elif isinstance(source, (DakodaPublicCorpusName, DakodaCorpusName)):
            corpus_name = source.value
            self.remote = True
            self._init_from_remote(corpus_name)
        elif isinstance(source, str):
            candidate_path = Path(source).expanduser()
            if candidate_path.exists():
                self.path = candidate_path
                self.name = candidate_path.stem
                self._init_from_filesystem(candidate_path)
            else:
                corpus_name = source.replace("_", "-") # allows users to pass corpus names with underscores instead of dashes
                self.remote = True
                self._init_from_remote(corpus_name, source)
        else:
            raise TypeError(
                "DakodaCorpus requires DakodaCorpusName, str or Path."
            )

    # =========================================================
    # Lokale Initialisierung
    # =========================================================
    def _init_from_filesystem(self, path: Path):

        if not path.exists():
            raise FileNotFoundError(f"Corpus path does not exist: {path}")

        resolved_path = path.resolve()

        print(f"[LOCAL LOAD] Loading corpus from: {resolved_path}")

        self.path = resolved_path
        self.name = resolved_path.stem

        self._document_paths = sorted(resolved_path.glob("*.xmi"))

        self._load_documents()

    # =========================================================
    # Remote Initialisierung
    # =========================================================
    def _init_from_remote(self, corpus_name: str, source_text: str | None = None):

        try:
            DakodaPublicCorpusName(corpus_name)
        except ValueError as exc:
            hint = ""
            if source_text is not None and self._looks_like_path_string(source_text):
                hint = " If this is a local path, pass an existing folder path."
            raise ValueError(
                f"Corpus '{corpus_name}' is not available for public download.{hint}"
            ) from exc

        self.name = corpus_name

        cache_path = self._get_cache_path(corpus_name)

        # -----------------------------------------------------
        # Bereits lokal vorhanden
        # -----------------------------------------------------
        if cache_path.exists():
            print(f"[CACHE LOAD] Using cached corpus: {corpus_name}")
            self._init_from_filesystem(cache_path)
            return

        # -----------------------------------------------------
        # Download notwendig
        # -----------------------------------------------------
        print(f"[REMOTE LOAD] Downloading corpus: {corpus_name}")

        self.CACHE_DIR.mkdir(parents=True, exist_ok=True)

        url = self._build_remote_url(corpus_name)

        try:
            print(f"Trying URL: {url}")

            response = requests.get(url, timeout=30)
            response.raise_for_status()

            print("Success with repository")

        except Exception as e:
            print(f"[URL FAILED] {e}")
            raise RuntimeError(
                f"Corpus '{corpus_name}' could not be downloaded from remote repository"
            ) from e

        cache_path.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(io.BytesIO(response.content), "r") as zf:
            zf.extractall(cache_path)

        self._init_from_filesystem(cache_path)

    # =========================================================
    # Cache Utilities
    # =========================================================
    @classmethod
    def _get_cache_path(cls, corpus_name: str) -> Path:
        return cls.CACHE_DIR / corpus_name

    @staticmethod
    def _build_remote_url(name: str) -> str:
        return f"https://dakoda.org/data/repo/open/{name}/{name}_xmi.zip"

    @staticmethod
    def _looks_like_path_string(text: str) -> bool:
        return (
            "/" in text
            or "\\" in text
            or text.startswith(".")
            or text.startswith("~")
        )

    # =========================================================
    # Dokumente laden
    # =========================================================
    def _load_documents(self):

        self._docs = []
        self._id_to_doc = {}

        for p in self._document_paths:
            doc = DakodaDocument(cas=None, id=p.stem, corpus=self)
            self._docs.append(doc)
            self._id_to_doc[doc.id] = doc

    # =========================================================
    # Standard API
    # =========================================================
    def __repr__(self):
        return f"DakodaCorpus(name={self.name}, path={self.path})"

    def __str__(self):
        return f"Dakoda Corpus: {self.name} at {self.path}"

    def __eq__(self, other):
        if not isinstance(other, DakodaCorpus):
            return False

        return self.path.resolve() == other.path.resolve()

    def __len__(self):
        return len(self._docs)

    def __iter__(self):
        return iter(self._docs)

    def __getitem__(self, key):

        if isinstance(key, Predicate):
            return self.__getitem__(self._query(key))

        elif isinstance(key, (str, Path)):
            return self._get_by_path(key)

        elif isinstance(key, int):
            return self._get_by_index(key)

        elif isinstance(key, slice):
            return self._get_by_slice(key)

        elif isinstance(key, Iterable):
            return [self.__getitem__(k) for k in key]

        else:
            raise KeyError(f"Invalid key type: {type(key)}")

    # =========================================================
    # Zugriff
    # =========================================================
    def _get_by_path(self, path: str | Path) -> DakodaDocument:
        return self._id_to_doc[Path(path).stem]

    def _get_by_index(self, index: int) -> DakodaDocument:
        return self._docs[index]

    def _get_by_slice(self, indices_slice: slice):
        start, stop, step = indices_slice.indices(len(self))
        return [
            self._get_by_index(i)
            for i in range(start, stop, step)
        ]

    # =========================================================
    # Indexing
    # =========================================================
    def _build_index(
        self,
        source_type: DataSubset | None = None,
        force_rebuild: bool = False,
    ):

        if source_type is None:
            self._build_index("cas")
            self._build_index("meta")
            return

        if (
            self._search_index.get(source_type) is not None
            and not force_rebuild
        ):
            return

        if source_type == "cas":
            indexer = CasIndexer()
            cache = IndexCache(self, source_type)

            if cache.is_cached and not force_rebuild:
                self._search_index[source_type] = cache.read()
                return

        elif source_type == "meta":
            indexer = MetaDataIndexer()
            cache = None

        else:
            raise ValueError(
                'Source Type must be either "cas", "meta" or None.'
            )

        self._search_index[source_type] = indexer.index_corpus(self)

        if cache is not None:
            cache.write(self._search_index[source_type])

    def _get_search_index(self, source_type: DataSubset):

        if source_type in DATA_SUBSETS:

            if self._search_index.get(source_type) is None:
                self._build_index(source_type)

            return self._search_index[source_type]

        else:
            raise ValueError(
                'Source Type must be either "cas", "meta" or None.'
            )

    def _query(
        self,
        q: Predicate,
        subset: DataSubset | None = None,
    ) -> List[int]:

        if subset in DATA_SUBSETS:
            idx = self._get_search_index(subset)
            return q.documents(idx).to_list()

        elif subset is None:
            result: set[int] = set()

            for s in DATA_SUBSETS:
                result.update(self._query(q, s))

            return list(result)

        else:
            raise ValueError(
                'Subset must be either "cas", "meta" or None.'
            )

    # =========================================================
    # Properties
    # =========================================================
    @property
    def size(self) -> int:
        return len(self)

    @property
    def docs(self):
        return self._docs.copy()

    @property
    def document_paths(self):
        return self._document_paths.copy()

    # =========================================================
    # Utility
    # =========================================================
    def random_doc(self) -> DakodaDocument:

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
        "idx": FieldMapping("idx", pl.Int64),
        "view": FieldMapping("view", pl.Categorical),
        "type": FieldMapping("type", pl.Categorical),
        "field": FieldMapping("field", pl.Categorical),
        "value": FieldMapping("value", pl.Object),
    }

    def __init__(self, field_mappings: dict[str, FieldMapping] | None = None):
        if field_mappings is None:
            field_mappings = self.default_field_mappings.copy()
        self.field_mappings = field_mappings

    @property
    def schema(self):
        return {
            field_mapping.name: field_mapping.dtype
            for field_mapping in self.field_mappings.values()
        }

    @property
    def column_mapping(self):
        return {name: mapping.name for name, mapping in self.field_mappings.items()}

    @abstractmethod
    def to_entries(self, doc: DakodaDocument, idx=None):
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
        "idx": FieldMapping("idx", pl.Int64),
        "view": FieldMapping("view", pl.Categorical),
        "type": FieldMapping("type", pl.Categorical),
        "field": FieldMapping("field", pl.Categorical),
        "value": FieldMapping("value", pl.Utf8),
    }

    def to_entries(self, doc: DakodaDocument, idx=None):
        entries = []
        cas = doc.cas
        for view_name, cas_view_name in view_to_name.items():
            view = cas.get_view(cas_view_name)
            for type_name, value_name in type_to_fieldname.items():
                annotations = view.select(type_name)
                for annotation in annotations:
                    if value_name == "coveredText":
                        value = annotation.get_covered_text()
                    else:
                        value = annotation[value_name]
                    entry = {
                        self.column_mapping.get("idx"): idx,
                        self.column_mapping.get("view"): view_name,
                        self.column_mapping.get("type"): type_name.split(".")[-1],
                        self.column_mapping.get("field"): value_name,
                        self.column_mapping.get("value"): value,
                    }
                    entries.append(entry)
        return entries


class MetaDataIndexer(Indexer):

    def to_entries(self, doc: DakodaDocument, idx=None):
        entries = []
        for key, value in doc.meta.iter_flat():
            entries.append(
                {
                    self.column_mapping.get("idx"): idx,
                    self.column_mapping.get("view"): None,
                    self.column_mapping.get("type"): None,
                    self.column_mapping.get("field"): key,
                    self.column_mapping.get("value"): value,
                }
            )
        return entries


class IndexCache:
    def __init__(
        self,
        corpus: DakodaCorpus,
        cache_name: DataSubset,
        cache_dir: str | Path | None = None,
    ):
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
