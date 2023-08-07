#!/usr/bin/env python3
"""
Module that type-annotates a function sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes in a list mxd_lst of integers and floats and returns their sum as
    a float
    """
    return sum(mxd_lst)
