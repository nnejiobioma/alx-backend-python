#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Any, Sequence, Union


from typing import Dict, TypeVar, Optional

# Create TypeVars for the key and value types
K = TypeVar('K')
V = TypeVar('V')

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> V:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Dict[K, V]): The dictionary.
        key (K): The key to look up.
        default (Optional[V]): The default value to return if the key is not found (default is None).

    Returns:
        V: The value associated with the key in the dictionary, or the default value if not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
