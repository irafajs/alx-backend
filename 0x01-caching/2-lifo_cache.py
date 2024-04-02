#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """method to define FIFO caching method"""
    def __init__(self):
        """reload init"""
        super().__init__()

    def put(self, key, item):
        """method to update the dictionay using FIFO"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_item = next(reversed(self.cache_data))
                print('DISCARD: {}'.format(last_item))
                del self.cache_data[last_item]
            self.cache_data[key] = item

    def get(self, key):
        """method to return valune in cache using the key args"""
        if key is not None:
            return self.cache_data.get(key)
