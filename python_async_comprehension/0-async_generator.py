#!/usr/bin/env python3
<<<<<<< HEAD
"""Async Generator"""

=======
'''Task 0
'''
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
<<<<<<< HEAD
    """Async Generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
=======
    '''Generate a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
