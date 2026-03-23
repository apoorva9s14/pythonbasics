from collections import OrderedDict
# LRU Cache — the canonical OrderedDict use case
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()     # key → value, ordered by recency

    def get(self, key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key)    # mark as most recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # evict least recently used (front)
lru_cache_size = 5
l = LRUCache(lru_cache_size)
l.set(1,1)