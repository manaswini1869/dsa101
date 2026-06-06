from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        n = len(nums)
        tots = sum(nums)
        left = 0
        ans = []
        for idx, curr in enumerate(nums):
            ans.append(abs(tots - left - curr))
            tots -= curr
            left += curr
        return ans

        # left = [0]*n
        # right = [0]*n
        # for i in range(n):
        #     left[i] = sum(nums[:i])
        #     right[i] = sum(nums[i+1:])

        # n = len(left)
        # ans = []
        # for i in range(n):
        #     ans.append(abs(left[i] - right[i]))

        # return ans


        