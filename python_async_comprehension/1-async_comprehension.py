#!/usr/bin/env python3
<<<<<<< HEAD
"""Async comprehension"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehension"""
    return [i async for i in async_generator()]
=======
'''Task 1
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a 10-number generator.
    '''
    return [num async for num in async_generator()]
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
