from __future__ import annotations

from dataclasses import dataclass

import cassis
from cassis import Cas
from cassis.typesystem import FeatureStructure
from importlib_resources import files


def load_dakoda_typesystem():
    type_system_str = files("dakoda.res").joinpath("dakoda_typesystem.xml").read_text()
    return cassis.load_typesystem(type_system_str)


def load_cas_from_file(path, ts):
    with open(path, "rb") as f:
        return cassis.load_cas_from_xmi(f, typesystem=ts)


def get_cas_meta_json_string(cas: Cas):
    for meta in cas.select(T_META):
        if meta.get("key") == "structured_metadata":
            return meta.get("value")


T_TOKEN = "de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token"
T_LEMMA = "de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Lemma"
T_POS = "de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS"
T_SENT = "de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Sentence"
T_MORPH = "de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.morph.Morpheme"
T_DEP = "de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency"
T_META = "de.tudarmstadt.ukp.dkpro.core.api.metadata.type.MetaDataStringField"
T_STAGE = "org.dakoda.Stage"

type_to_fieldname = {
    T_TOKEN: "coveredText",
    T_LEMMA: "value",
    T_POS: "PosValue",
    T_SENT: "coveredText",
    T_STAGE: "name",
}

view_to_name = {"learner": "ctok", "target_hypothesis": "mixtral_th1"}


@dataclass
class DocumentView:
    """Provides structured access to a specific view within a CAS document.

    Represents a particular view, such as learner text or target hypothesis.
    Offers convenient access to common linguistic annotations like tokens,
    sentences, and POS tags.

    Args:
        view_name: Name of the CAS view to access.
        cas: CAS object containing the document data.
    """
    view_name: str
    cas: Cas

    def __post_init__(self):
        self._view = self.cas.get_view(self.view_name)

    @property
    def text(self) -> str:
        """Get the raw text content of this document view.

        Returns:
            String containing the full text of this view.
        """
        return self._view.sofa_string

    def _raw_annotation(self, type_name):
        return self._view.select(type_name)

    def annotation(self, type_name: str):
        """Get all annotations of a specific type from this view.

        Retrieves and wraps raw CAS annotations in TypeAnnotation objects
        for easier access to annotation properties and text spans.

        Args:
            type_name: Fully qualified annotation type name to retrieve.

        Returns:
            List of TypeAnnotation objects for the specified type.

        Examples:
            >>> tokens = view.annotation(T_TOKEN)
            >>> custom_annos = view.annotation("my.custom.Type")
        """
        return [
            TypeAnnotation(type_name, anno) for anno in self._raw_annotation(type_name)
        ]

    @property
    def pos_tags(self):
        """Get all part-of-speech tag annotations from this view.

        Returns:
            List of TypeAnnotation objects for POS tags.
        """
        return self.annotation(T_POS)

    @property
    def lemmas(self):
        """Get all lemma annotations from this view.

        Returns:
            List of TypeAnnotation objects for lemmas.
        """
        return self.annotation(T_LEMMA)

    @property
    def tokens(self):
        """Get all token annotations from this view.

        Returns:
            List of TypeAnnotation objects for tokens.
        """
        return self.annotation(T_TOKEN)

    @property
    def sentences(self):
        """Get all sentence boundary annotations from this view.

        Returns:
            List of TypeAnnotation objects for sentences.
        """
        return self.annotation(T_SENT)

    @property
    def stages(self):
        """Get all processing stage annotations from this view.

        Returns:
            List of TypeAnnotation objects for processing stages.
        """
        return self.annotation(T_STAGE)


class TypeAnnotation:
    """Wrapper for UIMA CAS annotations providing convenient access to properties.

    Encapsulates a raw CAS annotation with its type information, offering
    easy access to covered text, feature values, and span information.
    Handles type-specific value extraction automatically.

    Args:
        type_name: Fully qualified name of the annotation type.
        annotation: Raw CAS FeatureStructure annotation object.
    """
    def __init__(self, type_name, annotation: FeatureStructure):
        self.type_name = type_name
        self.annotation = annotation

    @property
    def text(self):
        """Get the text covered by this annotation.

        Returns:
            String containing the text span covered by this annotation.
        """
        return self.annotation.get_covered_text()

    @property
    def value(self):
        """Get the primary feature value for this annotation type.

        Automatically extracts the most relevant feature value based on
        the annotation type, such as 'value' for lemmas or 'PosValue' for POS tags.

        Returns:
            The primary feature value for this annotation, or None if not applicable.
        """
        return self.annotation.get(type_to_fieldname[self.type_name])

    @property
    def span(self):
        """Get the character span boundaries of this annotation.

        Returns:
            Tuple of (begin, end) character positions in the document text.
        """
        return self.annotation.get("begin"), self.annotation.get("end")

    def __repr__(self):
        has_own_value = type_to_fieldname[self.type_name] is not None
        short_type_name = self.type_name.split(".")[-1]
        if has_own_value:
            return f"{short_type_name}({self.text}[{self.value}])"
        else:
            return f"{short_type_name}({self.text})"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if other is self:
            return True

        if not isinstance(other, TypeAnnotation):
            return False

        return (
            self.type_name == other.type_name
            and self.span == other.span
            and self.value == other.value
        )
