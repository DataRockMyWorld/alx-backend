#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching and
is a caching system.
You must use self.cache_data - dictionary from the parent class
BaseCaching
def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value
    for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher that
    BaseCaching.MAX_ITEMS:
    you must discard the first item put in cache (FIFO algorithm)
    you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist in self.cache_data, return None
"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class implements a caching system with LRU eviction policy."""

    def __init__(self):
        """Initialize the LRUCache."""
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: The key to add.
            item: The item to add.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.used_keys:
                self.used_keys.append(key)
            else:
                # Move the key to the end to show that it was recently used
                pop_key = self.used_keys.pop(self.used_keys.index(key))
                self.used_keys.append(pop_key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the first item in the list (the least recently used)
                discard = self.used_keys.pop(0)
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")

    def get(self, key):
        """Return the value in self.cache_data linked to key.

        Args:
            key: The key to retrieve.
        """
        if key is not None and key in self.cache_data:
            # Move the key to the end to show that it was recently used
            pop_key = self.used_keys.pop(self.used_keys.index(key))
            self.used_keys.append(pop_key)
            return self.cache_data[key]
        return None
