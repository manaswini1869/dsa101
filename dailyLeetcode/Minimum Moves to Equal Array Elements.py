import numpy as np

class Solution:
    def minMoves(self, nums: list[int]) -> int:

        minimum = min(nums)

        return sum(num - minimum for num in nums)

        # n = len(nums)
        # nums = np.array(nums)

        # if len(set(nums)) == 1:
        #         return 0

        # nums.sort()
        # count = 0 
        # for i in range(n-1):
        #     target = nums[i+1]        

        #     count += target - nums[i]
        #     nums += target - nums[i]
        #     nums[i+1] = target

        # return int(count)