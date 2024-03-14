#!/usr/bin/env python3

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple of string k and int/float v
    """
    return k, (v ** 2)
