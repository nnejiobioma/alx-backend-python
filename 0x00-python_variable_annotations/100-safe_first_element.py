#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element of a list if it exists, otherwise return None.

    Args:
        lst: Any iterable.

    Returns:
        The first element of lst if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
