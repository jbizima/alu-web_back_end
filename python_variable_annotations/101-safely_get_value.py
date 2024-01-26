#!/usr/bin/env python3
<<<<<<< HEAD
""""safely get value function"""

=======
'''Task 11
'''
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Retrieves a value from a dict using a given key.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
<<<<<<< HEAD

=======
    
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
