#!/usr/bin/env python3
"""
A complex types - list of floats
"""


from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of elements in a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing integers and floats.

    Returns:
        float: The sum of elements in the input list as a float.
    """
    return sum(mxd_lst)

