class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        num_zero = 0
        max_ones = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zero += 1
            while num_zero > 1:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1
            max_ones = max(max_ones, r - l)
        return max_ones
