#!/usr/bin/env python3
""" annotated function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multipliesa function """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
