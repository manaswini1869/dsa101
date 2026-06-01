from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> float:

        ans = float("inf")
        for num in nums:
            curr = 0
            while num:
                rem = num % 10
                curr += rem
                num = num // 10
            ans = min(ans, curr)
        return ans


        