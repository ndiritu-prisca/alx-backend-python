#!/usr/bin/env python3
"""
Module that contains a regular function that returns an asyncio.Task.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task for the wait_random coroutine with the specified
    max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
