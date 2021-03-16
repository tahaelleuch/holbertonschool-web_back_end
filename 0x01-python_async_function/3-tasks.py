#!/usr/bin/env python3
"""task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    [task]

    Args:
        max_delay (int): max

    Returns:
        asyncio.Task: a task
    """
    return asyncio.create_task(wait_random(max_delay))
