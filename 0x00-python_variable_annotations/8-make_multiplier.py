#!/usr/bin/env python3
"""
Module that type annotates function make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier
    """
    def multiplier_fn(value: float) -> float:
        """
        Function that multiples a float by multiplier
        """
        return value * multiplier
    return multiplier_fn
