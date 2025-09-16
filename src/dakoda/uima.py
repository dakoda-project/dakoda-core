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
    view_name: str
    cas: Cas

    def __post_init__(self):
        self._view = self.cas.get_view(self.view_name)

    @property
    def text(self) -> str:
        return self._view.sofa_string

    def _raw_annotation(self, type_name):
        return self._view.select(type_name)

    def annotation(self, type_name: str):
        return [
            TypeAnnotation(type_name, anno) for anno in self._raw_annotation(type_name)
        ]

    @property
    def pos_tags(self):
        return self.annotation(T_POS)

    @property
    def lemmas(self):
        return self.annotation(T_LEMMA)

    @property
    def tokens(self):
        return self.annotation(T_TOKEN)

    @property
    def sentences(self):
        return self.annotation(T_SENT)

    @property
    def stages(self):
        return self.annotation(T_STAGE)


class TypeAnnotation:
    def __init__(self, type_name, annotation: FeatureStructure):
        self.type_name = type_name
        self.annotation = annotation

    @property
    def text(self):
        return self.annotation.get_covered_text()

    @property
    def value(self):
        return self.annotation.get(type_to_fieldname[self.type_name])

    @property
    def span(self):
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
