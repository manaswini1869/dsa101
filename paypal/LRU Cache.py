class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = deque()


    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.lru.remove(key)
            self.lru.append(key)
            return
        if len(self.cache) == self.capacity:
            lru = self.lru.popleft()
            del self.cache[lru]
        self.cache[key] = self.cache.get(key, 0)
        self.cache[key] = value
        self.lru.append(key)
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)