#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ method to return data even some have been delete """
        assert index is None or isinstance(index, int)
        assert isinstance(page_size, int) and page_size > 0
        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        assert index is None or (0 <= index < total_items)
        start_index = index if index is not None else 0
        next_index = min(start_index + page_size, total_items)
        data = [indexed_dataset.get(i, None) for i in range(
            start_index, next_index)]
        data = [item for item in data if item is not None]
        hyper_deleted_metadata = {
                "index": start_index,
                "data": data,
                "page_size": page_size,
                "next_index": next_index
                }
        return hyper_deleted_metadata
