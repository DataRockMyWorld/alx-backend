#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to
call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the least frequency used item (LFU algorithm)
if you find more than 1 item to discard, you must use the LRU algorithm to
discard only the least recently used
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None
"""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """_summary_"""

    def __init__(self):
        """_summary_"""
        super().__init__()
        self.cache_data = {}
        self.freq = {}
        self.min_freq = 0

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item

def put(self, key, item):
        """Insert or update key/value pair in the cache

        Args:
            key (int): The key to be inserted or updated
            item (int): The value to be associated with the key
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discard_key = self.freq[self.min_freq].pop(0)
                del self.cache_data[discard_key]
                del self.freq[self.min_freq]

                if not self.freq[self.min_freq]:
                    del self.freq[self.min_freq]
                    self.min_freq += 1

            self.cache_data[key] = item

            if self.min_freq not in self.freq:
                self.freq[self.min_freq] = []
            self.freq[self.min_freq].append(key)
            self.min_freq = 1

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
