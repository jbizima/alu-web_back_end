#!/usr/bin/env python3
""""make_multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Computes a multiplier'''
        
    def multiply(n: float) -> float:
        """multiply function"""
        return n * multiplier
    return multiply

