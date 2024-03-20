#!/usr/bin/env python3

"""runtime form four parallel comprehensions"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    calculating runtime
    """
    start = time()
    tasks = [async_comprehension() for x in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
