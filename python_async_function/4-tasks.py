#!/usr/bin/env python3
<<<<<<< HEAD
'''concurent coroutines'''
import asyncio
from typing import List


=======
"""concurent coroutines"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
<<<<<<< HEAD
    '''Executes task_wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
=======
    """spawn wait_random n times with the specified max_delay"""
    tasks = [task_wait_random((max_delay)) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
