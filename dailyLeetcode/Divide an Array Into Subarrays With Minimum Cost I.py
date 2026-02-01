from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        n = len(nums)
        a = nums[0]
        b, c = float("inf"), float("inf")

        for num in nums[1:]:
            if num < c:
                b = c
                c = num
            elif num < b:
                b = num

        return a+b+c




        