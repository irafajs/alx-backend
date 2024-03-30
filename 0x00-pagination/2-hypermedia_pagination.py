#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """method that retunm start index and end index of a list"""
    offset = (page - 1) * page_size
    dataset = offset + page_size
    return (offset, dataset)


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
        """method to retrieve data using passend argument"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []
        return dataset[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ return a dictionary of page_size, page, data, next_page... """
        page_data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        start, end = index_range(page, page_size)
        total_pages = (total_items + page_size - 1) // page_size
        next_page = page + 1 if end < total_items else None
        prev_page = page - 1 if start > 0 else None
        hyper_metadata = {
                "page_size": len(page_data),
                "page": page,
                "data": page_data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
        return hyper_metadata
