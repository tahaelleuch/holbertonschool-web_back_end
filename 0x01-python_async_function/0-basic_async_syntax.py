#!/usr/bin/env python3
"""random wait"""

import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """make a random delay
    Args:
        max_delay (int, optional): max

    Return:
        float: wait time
    """
    rand = max_delay * random.random()
    await asyncio.sleep(rand)
    return rand
