#!/usr/bin/env python3
<<<<<<< HEAD
""""safe first element function"""

from typing import Any, List, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> List[Union[Any, None]]:
    ''' retrieve first element of a sequence'''
    if lst:
        return lst[0]
    else:
        return None

=======
'''
Return the first element of a list or none
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Return the first element of a list or none '''
    if lst:
        return lst[0]
    else:
        return None
>>>>>>> 5c626b3fad84610f777769272a0c38ac716fd55b
