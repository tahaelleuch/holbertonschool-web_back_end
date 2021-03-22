#!/usr/bin/python3
"""0-basic_cache.py
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class
    Args:
        BaseCaching ([class]): [BaseCaching module]
    """
    def put(self, key, item):
        """create
        Args:
            key(str): key to the dict
            item(str): value to be assigned
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get
        Args:
            key(str): key to the dict
        Returns:
            str / None: get value by key
        """
        return self.cache_data.get(key) or None
