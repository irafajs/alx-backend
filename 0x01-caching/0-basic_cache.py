#!/usr/bin/env python3
"""
Shebang to create a PY code
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """implment basic caching"""
    def put(self, key, item):
        """update the class with passed argument"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get value by passed key"""
        if key is not None:
            return self.cache_data.get(key)
