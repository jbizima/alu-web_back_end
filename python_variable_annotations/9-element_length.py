#!/usr/bin/env python3
<<<<<<< HEAD
""""element length function"""

=======
'''Task 9
'''
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
<<<<<<< HEAD
    ''' compute the length of a sequence'''
    return [(i, len(i)) for i in lst]

=======
    '''Computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
