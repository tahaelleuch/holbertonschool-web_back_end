#!/usr/bin/env python3
"""random wait"""

import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """make a random delay"""
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
