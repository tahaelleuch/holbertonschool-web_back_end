#!/usr/bin/python3
"""basic"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basiccash
    """
    def put(self, key, item):
        """put funcs

        Args:
            key(str): key to the dict
            item(str): value to be assigned
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get function

        Args:
            key(str): key to the dict

        Returns:
            str or None: get value by key
        """
        return self.cache_data.get(key) or None
