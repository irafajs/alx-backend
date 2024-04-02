#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """method to define MRU caching method"""
    def __init__(self):
        """reload init"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """method to update the dictionay using mru"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_item = self.order.pop()
                print('DISCARD:', mru_item)
                del self.cache_data[mru_item]
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """method to return valune in cache using the key args"""
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
