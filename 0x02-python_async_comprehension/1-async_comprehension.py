#1/usr/bin/env python3

"""async comprenhension"""

import random
async_generator = __import__('0-async_generator').async_generator
from typing import List

async def async_comprehension() -> List[int]:
    randnum = [number async for number in async_generator()]
    return randnum
