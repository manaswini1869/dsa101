from typing import List
class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:

        n = len(nums)
        if n < 2:
            return 0

        pre = nums[-1]

        for i in range(n-2, -1, -1):
            if nums[i] < pre:
                pre = nums[i]
            else:
                return i+1
        
        return 0


        # n = len(nums)
        # prefix = 0

        # for i in range(1, n):
        #     if nums[i-1] >= nums[i]:
        #         prefix = i
        
        # return prefix

        



        
        



        