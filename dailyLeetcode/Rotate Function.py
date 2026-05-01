from typing import List
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)
        curr = 0
        for i in range(n):
            curr += (i*nums[i])
        ans = curr
        total = sum(nums)
        for i in range(1, n):
            curr = curr + total - n * nums[n-i]
            ans = max(ans, curr)

        return ans





        