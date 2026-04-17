from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        def reverse(num):
            ans = 0
            while num > 0:
                ans = ans * 10 + num % 10
                num //= 10
            return ans

        seen = {}
        ans = float("inf")

        for j, num in enumerate(nums):
            if num in seen:
                ans = min(ans, j - seen[num])
            seen[reverse(num)] = j

        return -1 if ans == float("inf") else ans