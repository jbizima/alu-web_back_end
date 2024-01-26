#!/usr/bin/env python3
""""to_kv function"""

from typing import List, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    '''Computes a new tuple.
    '''     
    return (k, v*v)

