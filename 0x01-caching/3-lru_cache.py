#!/usr/bin/env python3
""" 3. LRU Caching system module
"""
import collections
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching system that uses the Least Recently Used algorithm
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()
        # self.cache_order = collections.OrderedDict()
        self.cache_order = []

    def put(self, key: str, item: any) -> None:
        """Add an item to the cache.
        If the key or item is none, method should not do anything
        If number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, the least recently used item in the cache is
        discarded.

        Args:
            key (str): The key to associate with the item.
            item (any): The item to be added to the cache.
        """
        if key is None or item is None:
            return
        # elif key in self.cache_order:
        #    self.cache_order.move_to_end(key)
        # elif len(self.cache_order) >= self.MAX_ITEMS:
        #    oldest_key = next(iter(self.cache_order))
        #     self.cache_order.pop(oldest_key)
        #     print("DISCARD: {}".format(oldest_key))

        # self.cache_order[key] = item
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                and key not in self.cache_data:
            print("Discard: {}".format(self.cache_order[0]))
            self.cache_data.pop(self.cache_order[0])
            del self.cache_order[0]
        elif key in self.cache_order:
            del self.cache_order[self.cache_order.index(key)]
        self.cache_order.append(key)
        self.cache_data[key] = item

    def get(self, key: str) -> any:
        """Retrieves an item fro the cache.

        Args:
            key (str): The key associated with the item to be retrieved.

        Returns:
            any: The item associated with the key or None if the key is not
            in the cache.
        """
        if key is None or key not in self.cache_order:
            return None

        # self.cache_order.move_to_end(key)
        # return self.cache_order[key]
        del self.cache_order[self.cache_order.index(key)]
        self.cache_order.append(key)
        return self.cache_data[key]
