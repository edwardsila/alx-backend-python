#!/usr/bin/env python3
""" annotated fn to strings an tuples """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple """
    return (k, float(v ** 2))
