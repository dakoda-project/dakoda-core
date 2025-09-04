import cassis
from importlib_resources import files


def load_dakoda_typesystem():
    type_system_str = files("dakoda.res").joinpath("dakoda_typesystem.xml").read_text()
    return cassis.load_typesystem(type_system_str)


def load_cas_from_file(path, ts):
    with open(path, "rb") as f:
        return cassis.load_cas_from_xmi(f, typesystem=ts)


T_TOKEN = "de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Token"
T_LEMMA = "de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Lemma"
T_POS = "de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.pos.POS"
T_SENT = "de.tudarmstadt.ukp.dkpro.core.api.segmentation.type.Sentence"
T_MORPH = "de.tudarmstadt.ukp.dkpro.core.api.lexmorph.type.morph.Morpheme"
T_DEP = "de.tudarmstadt.ukp.dkpro.core.api.syntax.type.dependency.Dependency"
T_META = "de.tudarmstadt.ukp.dkpro.core.api.metadata.type.MetaDataStringField"
