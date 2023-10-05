#!/usr/bin/env python3
"""
A complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate sum of elements a list containing.

    Args:
     mxd_lst (List[Union[int, float]]): list containing
     integers and floats.

    Returns:
        float: sum of elements in input list as a float.
    """
    return sum(input_list)
