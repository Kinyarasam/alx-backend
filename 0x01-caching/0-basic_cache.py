#!/usr/bin/env python3
""" 0. Basix dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BaseCaching a caching system that inherits from BaseCaching
    """

    def put(self, key, item):
        """Adds an item that allows storing and retrieving items
        from a dictionary

        Args:
            key:
            item:

        Returns:
            nothing if the key and item is none.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: __

        Returns:
            ___
        """
        return self.cache_data.get(key, None)
