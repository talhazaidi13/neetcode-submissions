class LRUCache:

    def __init__(self, capacity: int):
        self.lRUCache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        value = self.lRUCache.get(key , -1)
        if value == -1:
            return value
        else:
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
