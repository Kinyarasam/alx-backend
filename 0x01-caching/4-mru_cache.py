#!/usr/bin/env python3
"""MRU Caching algorithm module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A caching system that uses the Most Recently Used algorithm
    """

    def __init__(self):
        """Initialize MRUCache
        """

        super().__init__()
        self.cache_order = []

    def put(self, key: str, item: any) -> None:
        """Add an item to the cache.
        If the key or item is none, method should not do anything
        If number of items in self.cache_data is higher than
        BaseCaching.MAXITEMS, the most recently used item in the cache is discarded.

        Args:
            key (str): The key to associate with the item.
            item (any): The item to be added to be added to the cache
        """
        if key is None or item is None:
            return
        elif key in self.cache_data:
            self.cache_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # most recently used item is at the end of the list
            mru_key = self.cache_order.pop()
            self.cache_data.pop(mru_key)
            print("DISCARD: {}".format(mru_key))

        self.cache_data[key] = item
        self.cache_order.insert(0, key)

    def get(self, key: str) -> any:
        """Retrieve an item from the cache.

        Args:
            key (str): The key associated with the item to be retrieved.

        Returns:
            any: The item associated with the key or None if the key is not in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_order.remove(key)
        self.cache_order.insert(0, key)
        return self.cache_data[key]
