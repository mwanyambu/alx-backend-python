#!/usr/bin/env python3

"""
the wait function implemented
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    takses an integer argumentand waits for random  dely
    and eventually returns it
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
