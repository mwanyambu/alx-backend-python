#!/usr/bin/env python3

"""async comprenhension"""
from asyncio import sleep
from random import uniform
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine will collect 10 random ints over async_generator
    """
    randnum = [number async for number in async_generator()]
    return randnum
