#!/usr/bim/env python3

"""measure the runtime"""

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """measure total execution time for waint_n"""

    start = time()
    run(wait_n(n, max_delay))
    end = time()

    return (end - start) / n
