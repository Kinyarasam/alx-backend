#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""


import csv
import math
from typing import Dict, List


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
        """Given a start index and a page size, returns a dictionary
        containing the following key-value pairs:
        index: the currnet start of the return page. That is the index
            of the first item in the current page.
        next_index: the next index to query with. That should be the index of
            the first item after the last item on the current page
        page_size: the current page size
        data: the actual page of the dataset

        Args:
            index (int, optional): the starting index of the page.
                Defaults to None
            page_size (int, optional): the size of the page. Defaults to 10.

        Returns:
            Dict: a dictionary coontaining the key-value pairs:
                index, next_index, pagesize, data

        Raises:
            AssertionError: if the index is out of range of the dataset
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(
                data.keys()), "Index out of range"
        page_data = []
        data_count = 0
        next_index = None
        start = index if index else 0
        for i, item in data.items():
            if i >= start and data_count < page_size:
                page_data.append(item)
                data_count += 1
                continue
            if data_count == page_size:
                next_index = i
                break
        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
        return page_info
