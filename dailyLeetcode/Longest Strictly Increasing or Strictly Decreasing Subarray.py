class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        ans = 1
        inc, dec = 1, 1
        n = len(nums)
        i = 0
        while i < n-1:
            if nums[i] > nums[i+1]:
                dec += 1
                inc = 1
                ans = max(ans, dec)
            elif nums[i] < nums[i+1]:
                inc += 1
                dec = 1
                ans = max(ans, inc)
            else:
                inc = 1
                dec = 1
            i += 1
        return ans
