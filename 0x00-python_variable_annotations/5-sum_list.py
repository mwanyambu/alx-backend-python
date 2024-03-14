#!/usr/bin/env python3
"""
sum of list items
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    takes a list of floats and returns their sum
    """
    result: float = 0
    for i in input_list:
        result += i
    return result
