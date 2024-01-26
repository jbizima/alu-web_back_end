#!/usr/bin/env python3
""""sum mixed list from inputed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''Computes the sum of a mixed list of float and integer numbers.
    '''     
    return float(sum(mxd_lst))

