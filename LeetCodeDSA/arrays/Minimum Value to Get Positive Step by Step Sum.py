class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        n = len(nums)

        p = [nums[0]]

        res = nums[0]
        min_val = float("inf")
        for i in range(1, n):
            p.append(p[-1] + nums[i])
            res = min(res, p[-1])

        return max(1, 1-res)

