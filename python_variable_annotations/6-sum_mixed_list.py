#!/usr/bin/env python3
<<<<<<< HEAD
""""sum mixed list from inputed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''Computes the sum of a mixed list of float and integer numbers.
    '''     
    return float(sum(mxd_lst))

=======
'''Task 6
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Computes the sum of a list of integers and floating-point numbers.
    '''
    return float(sum(mxd_lst))
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
