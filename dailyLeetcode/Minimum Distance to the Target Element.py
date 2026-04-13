from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        ans = float("inf")

        for idx, val in enumerate(nums):
            if val == target:
                ans = min(ans, abs(start - idx))

        return ans

