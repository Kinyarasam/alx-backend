#!/usr/bin/env python3
"""
Helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Given a page number and a page size, returns a tuple of size two containing
    the start and end index corresponding to the range of indexes to return in
    a list for those particular parameters.

    Args:
        page (int): The page number, 1-indexed.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple of size two containing the start and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
