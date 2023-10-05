#!/usr/bin/env python3
"""
This Type annotated function
for advance used
"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
     """
      Safely get a value from a dictionary.

      Args:
        dct (Dict[K, V]): The dictionary.
        key (K): The key to look up.
        default (Optional[V]): The default value to return
        if the key is not found (default is None).

      Returns:
        V: The value associated with the key in the
        dictionary, or the default value if not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
