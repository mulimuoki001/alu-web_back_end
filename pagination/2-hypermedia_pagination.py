#!/usr/bin/env python3


"""
pagination helper function
"""
import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        dict1 = {
            "page_size": page_size,
            "page": page,
            "data": self.dataset()[start:end],
            "next_page": page + 1 if end < len(self.dataset()) else None,
            "prev_page": page - 1 if start > 0 else None,
            "total_pages": len(self.dataset()),
        }
        return dict1


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    the given pagination parameters.
    """
    return (page - 1) * page_size, page * page_size
