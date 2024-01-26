#!/usr/bin/env python3
<<<<<<< HEAD
""""zoom array function"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Creates multiple copies of items in a tuple.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
=======
'''
Type checking
'''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    ''' Type checking '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
    ]
    return zoomed_in


<<<<<<< HEAD
array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

=======
array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
