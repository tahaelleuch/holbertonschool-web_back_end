#!/usr/bin/python3
"""
1-fifo_cache.py
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class
     Args:
        BaseCaching(class): BaseCaching module
    """
    def __init__(self):
        """
        init
        """
        super().__init__()
        self.current_cache = []

    def put(self, key, item):
        """create
        Args:
            key(str): key to the dict
            item(str): value to be assigned
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.current_cache:
                self.current_cache.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.current_cache.pop(0)
                del self.cache_data[discarded]
                print("DISCARD: {}".format(discarded))

    def get(self, key):
        """get
        Args:
            key(str): key to the dict
        Returns:
            str / None: get value by key
        """
        return self.cache_data.get(key) or None
