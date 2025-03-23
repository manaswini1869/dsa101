class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        self.hash_map[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.hash_map:
            last_ele, idx = self.array[-1], self.hash_map[val]
            self.array[idx], self.hash_map[last_ele] = last_ele, idx

            self.array.pop()
            del self.hash_map[val]

            return True
        return False

    def getRandom(self) -> int:
        return choice(self.array)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()