#!/usr/bin/env python3

from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list of tuples where each tuple contains an element from input
    """
    return [(x, len(x)) for x in lst]
