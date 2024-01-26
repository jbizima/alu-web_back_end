#!/usr/bin/env python3
<<<<<<< HEAD
""""to_kv function"""

from typing import List, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    '''Computes a new tuple.
    '''     
    return (k, v*v)

=======
'''Task 7
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple of the key and
    the square of its value.
    '''
    return (k, float(v**2))
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
