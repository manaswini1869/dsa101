class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.p = [nums[0]]
        for i in range(1, self.n):
            self.p.append(self.p[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.p[right]
        return self.p[right] - self.p[left-1]

        # prefix[j] - prefix[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)