from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        # n = len(nums)
        # i = 0
        # while i < n-1 and nums[i] < nums[i+1]:
        #     i += 1
        # if i == n-1:
        #     return nums[0]
        # return nums[i+1] 
        n = len(nums)
        l = 0
        r = n-1
        res = nums[l]
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            mid = int(l+r/2)
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l += 1
            else:
                r -= 1
        return res
        