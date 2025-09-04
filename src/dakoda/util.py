import cassis
from importlib_resources import files


def load_dakoda_typesystem():
    type_system_str = files("dakoda.res").joinpath("dakoda_typesystem.xml").read_text()
    return cassis.load_typesystem(type_system_str)


def load_cas_from_file(path, ts):
    with open(path, "rb") as f:
        return cassis.load_cas_from_xmi(f, typesystem=ts)
