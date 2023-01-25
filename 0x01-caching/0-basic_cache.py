#!/usr/bin/env python3
""" 0. Basix dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BaseCache class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Initialize an empty cache_data dictionary and MAX_ITEMS
        """
        super().__init__()

    def put(self, key, item):
        """Put an item in the cache_data dictionary

        Args:
            key (str): key to be used as an index
            item: item to be stored

        Returns:
            nothing if the key and item is none.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get the item from cache_data

        Args:
            key(str): key to get the item

        Returns:
            the item or None if the the key does not exist
        """
        return self.cache_data.get(key, None)
