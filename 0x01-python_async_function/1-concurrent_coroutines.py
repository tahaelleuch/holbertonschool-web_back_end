#!/usr/bin/env python3
"""wait_random"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    [random]

    Args:
        n (int): n
        max_delay (int, optional): max

    Returns:
        List[float]: the wait time
    """
    spawn_list = []
    delay_list = []
    for x in range(n):
        spawn_list.append(wait_random(max_delay))
    for task in asyncio.as_completed(spawn_list):
        delay_list.append(await task)
    return delay_list
