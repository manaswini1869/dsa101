class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # for i in range(n+1):
        #     if i not in nums:
        #         return i
        # nums.sort()

        # for k, v in enumerate(nums):
        #     if k != v:
        #         return k
        #     if v == len(nums) - 1:
        #         return k + 1
        return sum(range(len(nums)+1)) - sum(nums)
