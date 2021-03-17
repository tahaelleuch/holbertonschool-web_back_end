#!/usr/bin/env python3
"""0-async_generator.py"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    [Generator]

    Yields:
        List[float]: res
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
