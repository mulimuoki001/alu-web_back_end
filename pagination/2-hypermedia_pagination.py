#!/usr/bin/env python3

"""
Pagination helper function
"""

import csv
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The file path to the dataset.
        __dataset (List[List]): The cached dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the cached dataset.

        If the dataset is not cached, it reads the
        dataset from the file and caches it.

        Returns:
            List[List]: The dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns the appropriate page of the dataset.

        Args:
            page (int): The page number. Defaults to 1.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            dict: A dictionary containing the page data, including:
                - page_size (int): The number of items per page.
                - page (int): The current page number.
                - data (List[List]): The data for the current page.
                - next_page (int): The next page number, or None
                if there is no next page.
                - prev_page (int): The previous page number, or
                None if there is no previous page.
                - total_pages (int): The total number of pages.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.dataset()):
            return {
                "page_size": page_size,
                "page": page,
                "data": [],
                "next_page": None,
                "prev_page": None,
                "total_pages": len(self.dataset()),
            }
        dict1 = {
            "page_size": page_size,
            "page": page,
            "data": self.dataset()[start:end],
            "next_page": page + 1 if end < len(self.dataset()) else None,
            "prev_page": page - 1 if start > 0 else None,
            "total_pages": len(self.dataset()),
        }
        if end >= len(self.dataset()):
            dict1["next_page"] = None
        return dict1


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for
    the given pagination parameters.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    return (page - 1) * page_size, page * page_size
