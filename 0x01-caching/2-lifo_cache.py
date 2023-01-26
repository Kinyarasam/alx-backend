#!/usr/bin/env python3
"""Last-In First-Out caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system that uses the Last In First Out (LIFO) algorithm.
    """

    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_order = []

    def put(self, key: str, item: any) -> None:
        """Add an item to the cache.
        If the key or item is None, method should not do anything
        If number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, the last item put in the cache is discarded.

        Args:
            key (str): The key associated with the item.
            item (any): The item to be added to the cache.
        """
        if key is None or item is None:
            return
        elif key in self.cache_data:
            self.cache_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            last_item_key = self.cache_order.pop()
            self.cache_data.pop(last_item_key)
            print("DISCARD: {}".format(last_item_key))

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
        if key is none or key not in self.cache_data:
            return None

        return self.cache[key]
