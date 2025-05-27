# from collections import Counter
# class FirstUnique:

#     def __init__(self, nums: List[int]):
#         self.nums = Counter(nums)
#         self.unique = -1
#         for key,value in self.nums.items():
#             if value == 1:
#                 self.unique = key
#                 break
#     def showFirstUnique(self) -> int:
#         return self.unique

#     def add(self, value: int) -> None:
#         self.nums[value] = self.nums.get(value, 0) + 1
#         for key,value in self.nums.items():
#             if value == 1:
#                 self.unique = key
#                 break
#             else:
#                 self.unique = -1

from collections import deque, Counter

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.nums_map = Counter()
        self.queue = deque()

        for num in nums:
            self.add(num)

    def add(self, value: int) -> None:
        self.nums_map[value] += 1
        if self.nums_map[value] == 1:
            self.queue.append(value)

    def showFirstUnique(self) -> int:
        while self.queue and self.nums_map[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)