#!/usr/bin/env python3
"""2-measure_runtime.py"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    [time]

    Returns:
        float: res
    """
    start = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return (time.time() - start)
