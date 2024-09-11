#!/usr/bin/env python3


"""
pagination helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    the given pagination parameters.
    """
    return (page - 1) * page_size, page * page_size
