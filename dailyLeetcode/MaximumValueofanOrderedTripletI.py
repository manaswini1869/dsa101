from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [0] * n
        max_right = [0] * n

        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], nums[i])

        max_right[-1] = nums[-1]
        for k in range(n - 2, -1, -1):
            max_right[k] = max(max_right[k + 1], nums[k])

        res = 0
        for j in range(1, n - 1):
            max_i = max_left[j - 1]
            max_k = max_right[j + 1]
            res = max(res, (max_i - nums[j]) * max_k)

        return res
