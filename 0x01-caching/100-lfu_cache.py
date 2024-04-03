#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """method to define LFU caching method"""
    def __init__(self):
        """reload init"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """method to update the dictionay using LFU"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                lfu_items = [key for key, freq in self.frequency.items(
                    ) if freq == min_frequency]
                if len(lfu_items) > 1:
                    lfu_item = min(self.cache_data, key=self.cache_data.get)
                else:
                    lfu_item = lfu_items[0]
                print('DISCARD:', lfu_item)
                del self.cache_data[lfu_item]
                del self.frequency[lfu_item]
            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """method to return valune in cache using the key args"""
        if key is not None:
            if key in self.cache_data:
                self.frequency[key] = self.frequency.get(key, 0) + 1
                return self.cache_data.get(key)
        return None
