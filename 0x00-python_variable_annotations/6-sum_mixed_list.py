#!/usr/bin/env python 3

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list with different data types ints and floats and returns float
    """
    return sum(mxd_lst)
