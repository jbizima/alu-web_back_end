#!/usr/bin/env python3
<<<<<<< HEAD
""""make_multiplier function"""

=======
'''Task 8
'''
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
<<<<<<< HEAD
    '''Computes a multiplier'''
        
    def multiply(n: float) -> float:
        """multiply function"""
        return n * multiplier
    return multiply

=======
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
