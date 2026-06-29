class LRUCache:

    def __init__(self, capacity: int):
        self.lRUCache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.lRUCache:
            return -1
        # # Move to most recent by re-inserting at end
        # value = self.lRUCache.pop(key)      # ✅ remove from current position
        value = self.lRUCache.get(key , -1)
        if value != -1:
            del self.lRUCache[key]
        self.lRUCache[key] = value          # ✅ re-insert at end (most recent)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.lRUCache:
            del self.lRUCache[key]          
        elif len(self.lRUCache) >= self.cap:
            oldest = next(iter(self.lRUCache))
            del self.lRUCache[oldest]
        self.lRUCache[key] = value
