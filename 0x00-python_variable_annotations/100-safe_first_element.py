#!/usr/bin/env python3
"""
Module that duck-types safe_first_element
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function that is to be duck-typed
    """
    if lst:
        return lst[0]
    else:
        return None
