#!/usr/bin/env python3
"""async generator"""
import random
import asyncio


async def async_generator():
    """
    coroutine will loop 10 times asynchronously wait 1 sec and yeild random num
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
