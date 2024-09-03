#!/usr/bin/env python3
from typing import List


"""
This module contains a function that
sums all elements in a list.

Example:
    >>> sum_list([1, 2, 3, 4])
    10
    >>> sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    55
"""


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of all elements in a list.

    Args:
        input_list (list): The list to sum.

    Returns:
        int: The sum of all elements in the list.

    Example:
        >>> sum_list([1, 2, 3, 4])
    """
    return sum(input_list)
