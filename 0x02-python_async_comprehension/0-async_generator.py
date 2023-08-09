#!/usr/bin/env python3
"""
Module that writes a coroutine async_generator
"""

import asyncio
import random


async def async_generator() -> float:
    """
    The function takes no argument, loops the coroutine 10 times,
    asynchronously waits 1 second and yields a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
