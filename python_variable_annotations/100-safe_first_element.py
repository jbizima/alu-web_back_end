#!/usr/bin/env python3
""""safe first element function"""

from typing import Any, List, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> List[Union[Any, None]]:
    ''' retrieve first element of a sequence'''
    if lst:
        return lst[0]
    else:
        return None

