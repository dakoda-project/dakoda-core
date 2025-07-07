import cassis
import polars as pl
from importlib_resources import files
from dataclasses import fields, is_dataclass
from dakoda.dakoda_metadata_scheme import LanguageOfSpeaker, Annotation
from typing import Any, Generator, Tuple

def load_dakoda_typesystem():
    type_system_str = files('dakoda.res').joinpath('dakoda_typesystem.xml').read_text()
    return cassis.load_typesystem(type_system_str)
    
    #with open("dakoda/res/dakoda_typesystem.xml", 'rb') as f:
    #    return cassis.load_typesystem(f)

def load_cas_from_file(path, ts):
    with open(path, 'rb') as f:
        return cassis.load_cas_from_xmi(f, typesystem=ts)

def traverse_dataclass(obj: Any, path: str = "") -> Generator[Tuple[str, Any], None, None]:
    """Generator that yields (path, value) tuples for leaf nodes only"""
    if hasattr(obj, '__dataclass_fields__'):
        for field in fields(obj):
            
            field_value = getattr(obj, field.name)
            current_path = f"{path}.{field.name}" if path else field.name

            print('t:', current_path, ' - ', type(field_value))
            if type(field_value) == LanguageOfSpeaker or type(field_value) == Annotation:
            # elif isinstance(field_value, (LanguageOfSpeaker, Annotation)):
                # Special handling for LanguageOfSpeaker and Annotation
                ######## TODO
                # for now ignore, see how this can be treated later
                print("----------- HIER -------------")
                pass

            # Only yield if this is a leaf node (not a nested dataclass)
            if hasattr(field_value, '__dataclass_fields__'):
                # This is a nested dataclass, recurse but don't yield
                yield from traverse_dataclass(field_value, current_path)
            else:
                if isinstance(field_value, list):

                    # TODO needs to be handled better
                    # for now only return first element of list
                    if len(field_value) > 0:
                        field_value = field_value[0]
                        if hasattr(field_value, '__dataclass_fields__'):
                            yield from traverse_dataclass(field_value, current_path)
                        elif type(field_value) == LanguageOfSpeaker or type(field_value) == Annotation:
                        # elif isinstance(field_value, (LanguageOfSpeaker, Annotation)):
                            # Special handling for LanguageOfSpeaker and Annotation
                            ######## TODO
                            # for now ignore, see how this can be treated later
                            print("----------- HIER -------------")
                            pass
                    else:
                        field_value = ""

                # This is a leaf node, yield it
                yield (current_path, field_value)

def traverse_complex(obj: Any, depth: int = 0) -> Generator[Tuple[str, Any], None, None]:
    
    # Prevent infinite recursion with circular references
    obj_id = id(obj)
    
    if is_dataclass(obj):
        indent = "  " * depth
        #print(f"{indent}{type(obj).__name__}:")
        
        for field in fields(obj):
            field_value = getattr(obj, field.name)
            #print(f"{indent}  {field.name}: ", end="")
            
            if field_value is None:
                #print("None")
                pass
            elif is_dataclass(field_value):
                #print()
                yield from traverse_complex(field_value, depth + 2)
            elif isinstance(field_value, (list, tuple)):
                #print(f"[{len(field_value)} items]")
                for i, item in enumerate(field_value):
                    if is_dataclass(item):
                        #print(f"{indent}    [{i}]:")
                        yield from traverse_complex(item, depth + 3)
                    else:
                        #print(f"{indent}    [{i}]: {item}")
                        yield(field.name, item)
            elif isinstance(field_value, dict):
                print(f"dict with {len(field_value)} items")
                for key, value in field_value.items():
                    if is_dataclass(value):
                        #print(f"{indent}    {key}:")
                        yield from traverse_complex(value, depth + 3)
                    else:
                        print(f"{indent}    {key}: {value}")
                        yield(key, value)
            else:
                yield(field.name, field_value)

# def traverse_complex(obj: Any, depth: int = 0) -> None:
    
#     # Prevent infinite recursion with circular references
#     obj_id = id(obj)
    
#     if is_dataclass(obj):
#         indent = "  " * depth
#         print(f"{indent}{type(obj).__name__}:")
        
#         for field in fields(obj):
#             field_value = getattr(obj, field.name)
#             print(f"{indent}  {field.name}: ", end="")
            
#             if field_value is None:
#                 print("None")
#             elif is_dataclass(field_value):
#                 print()
#                 traverse_complex(field_value, depth + 2)
#             elif isinstance(field_value, (list, tuple)):
#                 print(f"[{len(field_value)} items]")
#                 for i, item in enumerate(field_value):
#                     if is_dataclass(item):
#                         print(f"{indent}    [{i}]:")
#                         traverse_complex(item, depth + 3)
#                     else:
#                         print(f"{indent}    [{i}]: {item}")
#             elif isinstance(field_value, dict):
#                 print(f"dict with {len(field_value)} items")
#                 for key, value in field_value.items():
#                     if is_dataclass(value):
#                         print(f"{indent}    {key}:")
#                         traverse_complex(value, depth + 3)
#                     else:
#                         print(f"{indent}    {key}: {value}")
#             else:
#                 print(field_value)
