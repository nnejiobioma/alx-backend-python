#!/usr/bin/env python3
"""
Takes list as input of float
and returns sum of float
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculate sum of the elements in a list of floats.

    Args:
        input_list (List[float]): list of floats to be summed.

    Returns:
        float: Sum of elements in the input list as a float.
    """
    return sum(input_list)
