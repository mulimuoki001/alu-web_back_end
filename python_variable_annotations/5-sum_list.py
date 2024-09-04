#!/usr/bin/env python3


"""
This module contains a function that
sums all elements in a list.
import List from typing
"""
from typing import List

"""
This module contains a function that sums all elements in a list.

Example:
    >>> sum_list([1, 2, 3, 4])
    10
    >>> sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    55
"""


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of all elements in a list.

    Args:
        input_list (List[float]): The list to sum.
        The list can contain floating point numbers.

    Returns:
        float: The sum of all elements in the list.

    Example:
        >>> sum_list([1, 2, 3, 4])
        10
    """
    return sum(input_list)