#!/usr/bin/env python3
""""element length function"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' compute the length of a sequence'''
    return [(i, len(i)) for i in lst]

