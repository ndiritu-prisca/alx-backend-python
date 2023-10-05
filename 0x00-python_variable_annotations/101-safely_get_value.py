#!/usr/bin/env python3
"""
Module that duck-types safely_get_value
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """
    Function that is to be duck-typed
    """
    if key in dct:
        return dct[key]
    else:
        return default
