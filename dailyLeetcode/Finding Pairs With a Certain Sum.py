class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq1 = defaultdict(int)
        self.freq2 = defaultdict(int)
        for i in self.nums1:
            self.freq1[i] += 1
        for i in self.nums2:
            self.freq2[i] += 1

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]

        self.nums2[index] += val
        new_val = self.nums2[index]
        self.freq2[new_val] += 1

    def count(self, tot: int) -> int:
        count = 0
        for key, val in self.freq1.items():
            needed = tot - key
            if needed in self.freq2:
                count += val * self.freq2[needed]
        return count



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)