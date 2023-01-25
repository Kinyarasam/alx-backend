#!/usr/bin/env python3
"""First In First Out caching module.
"""
import collections
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system that uses the First In First Out (FIFO) algorithm
    """
    def __init__(self):
        super().__init__()
        self.cache_order = collections.deque()

    def put(self, key: str, item: any) -> None:
        """Add an item to the cache.
        If the key or item is none, method should not do anything
        If number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, the oldest item in the cache is discarded.

        Args:
            key (str): The key to associate with the item.
            item (any): The item to be added to the cache.
        """
        if key is None or item is None:
            return
        elif key in self.cache_data:
            self.cache_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key = self.cache_order.popleft()
            self.cache_data.pop(oldest_key)
            print("DISCARD:", oldest_key)

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key: str) -> any:
        """Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item to be retrieved.

        Returns:
            any: The item associated with the key or None if the key is not
                in the cache.
        """
        # return self.cache_data.get(key, None)
        if key is None or key not in self.cache_data:
            return None

        return self.cache[key]
