#!/usr/bin/env python3
"""task_two"""

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    [task_two]

    Args:
        n (int): number
        max_delay (int, optional): max

    Returns:
        List[float]: res
    """
    spawn_list = []
    delay_list = []
    for x in range(n):
        spawn_list.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(spawn_list):
        delay_list.append(await task)
    return delay_list