#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching and
is a caching system.
You must use self.cache_data - dictionary from the parent class BaseCaching
def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
    you must discard the first item put in cache (FIFO algorithm)
    you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None

"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """FifoCache defines:"""
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = {}
        
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            print("DISCARD: {}".format(last_key))
            del self.cache_data[last_key]
        self.cache_data[key] = item


    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
    

