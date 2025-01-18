import collections

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the cache with a fixed capacity.
        self.cap = capacity
        # Use OrderedDict to maintain the order of items in cache.
        # OrderedDict keeps the items in the order they were added,
        # allowing easy access to the least recently used (LRU) item.
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        # If the key is not in the cache, return -1.
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to mark it as recently used.
        self.makeRecently(key)
        # Return the value associated with the key.
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If the key is already in the cache:
        if key in self.cache:
            # Update the key with the new value.
            self.cache[key] = value
            # Move the key to the end to mark it as recently used.
            self.makeRecently(key)
            return

        # If the cache is at full capacity:
        if len(self.cache) >= self.cap:
            # Remove the oldest item (the first item in OrderedDict).
            oldestKey = next(iter(self.cache))
            self.cache.pop(oldestKey)

        # Add the new key-value pair to the cache.
        # By default, OrderedDict adds new items to the end.
        self.cache[key] = value

    def makeRecently(self, key: int) -> None:
        # Remove the key from its current position
        # and reinsert it at the end to mark it as recently used.
        value = self.cache.pop(key)
        self.cache[key] = value
