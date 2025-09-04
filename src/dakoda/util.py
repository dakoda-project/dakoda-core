import csv

import cassis
from importlib_resources import files
from importlib_resources.abc import Traversable
from enum import Enum
from pathlib import Path


def load_dakoda_typesystem():
    type_system_str = files("dakoda.res").joinpath("dakoda_typesystem.xml").read_text()
    return cassis.load_typesystem(type_system_str)


def load_cas_from_file(path, ts):
    with open(path, "rb") as f:
        return cassis.load_cas_from_xmi(f, typesystem=ts)

def enum_from_file(file_path: str | Path | Traversable, separator=','):
    """Creates an enum from a csv file.
    Assumes two columns, first one containing keys, second one values.

    Note:
        Enums created in this way will not have IDE support. This should be fine, as these Enums are only used by the JSONParser in the metadata parsing.
    """
    def decorator(cls):
        enum_dict = {}
        with Path(file_path).open('r') as f:
            reader = csv.reader(f, delimiter=separator)
            for row in reader:
                if not row or len(row) < 2:
                    continue

                key = row[0].strip()
                value = row[1].strip()
                if key:
                    enum_dict[key] = value

        return Enum(cls.__name__, enum_dict)

    return decorator