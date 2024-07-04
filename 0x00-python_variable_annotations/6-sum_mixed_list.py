#!/usr/bin/env python3
""" annotated function to return mxd list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns sum of the mxd list """
    return sum(mxd_lst)
