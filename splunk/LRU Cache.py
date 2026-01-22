class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.q = deque()


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.q.remove(key)
        self.q.append(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.q.remove(key)
            self.q.append(key)
            self.map[key] = value
        else:
            while len(self.map) == self.cap:
                val = self.q.popleft()
                del self.map[val]
            self.q.append(key)
            self.map[key] = self.map.get(key, value)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)