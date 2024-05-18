#!/usr/bin/env python3
"""
class Server:
"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """
    Function that returns a page of the dataset
    Parameters:
        page (int): Page number
        page_size (int): Number of items per page

    Returns:
        List[List]: List of rows representing the page data
    """
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    try:
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
    except IndexError:
        return []


def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
    """
    Implement a get_hyper method that takes the same arguments
    (and defaults) as get_page
    and returns a dictionary containing the following key-value pairs:

    page_size: the length of the returned dataset page
    page: the current page number
    data: the dataset page (equivalent to return from previous task)
    next_page: number of the next page, None if no next page
    prev_page: number of the previous page, None if no previous page
    total_pages: the total number of pages in the dataset as an integer
    Make sure to reuse get_page in your implementation.

    You can use the math module if necessary.
    """
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0
    data = self.get_page(page, page_size)
    total_pages = math.ceil(len(self.dataset()) / page_size)
    return {
        'page_size': len(data),
        'page': page,
        'data': data,
        'next_page': page + 1 if page < total_pages else None,
        'prev_page': page - 1 if page > 1 else None,
        'total_pages': total_pages
    }
