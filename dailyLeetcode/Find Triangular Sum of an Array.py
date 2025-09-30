class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]

        n = len(nums)
        new = []
        for i in range(n-1 ):
            new.append((nums[i] + nums[i+1]) % 10)
        return self.triangularSum(new)


