#!/usr/bin/python3
"""basic"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basiccash
    """
    def put(self, key, item):
        """put funcs"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        return self.cache_data.get(key) or None
