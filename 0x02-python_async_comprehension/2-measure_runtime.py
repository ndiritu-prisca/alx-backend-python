#!/usr/bin/env python3
"""
Module that writes measure_runtime coroutine
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather,
    measures the total runtime, and returns it.
    """
    start_time = asyncio.get_event_loop().time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime
