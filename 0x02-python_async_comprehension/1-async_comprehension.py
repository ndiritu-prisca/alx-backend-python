#!/usr/bin/env python3
"""
Module that writes a coroutine async_comprehension
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    The coroutine collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers
