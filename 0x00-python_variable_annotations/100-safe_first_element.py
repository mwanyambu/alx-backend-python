#!/usr/bin/env python3

from typing import Any, Union, Sequence

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns first element of input list if exists else None
    """
    if lst:
        return lst[0]
    else:
        return None
