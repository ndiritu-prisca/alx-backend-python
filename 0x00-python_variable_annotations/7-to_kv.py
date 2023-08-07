#!/usr/bin/env python3
"""
Module that type-annotates function to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that takes a string k and an int OR float v as arguments and
    returns a tuple
    """
    squared_v = v ** 2
    return k, squared_v
