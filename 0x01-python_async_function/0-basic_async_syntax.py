#!/usr/bin/env python3
"""
    Module that contains an asynchronous coroutine that
    waits for a random delay and returns it.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


