#!/usr/bin/env python3
"""async generator"""
from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine will loop 10 times asynchronously wait 1 sec and yeild random num
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
