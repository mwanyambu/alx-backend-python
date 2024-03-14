#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies multiplier by callable float
    """
    def return_function(i: float) -> float:
        return i * multiplier
    return return_function
