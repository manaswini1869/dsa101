class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        l = 0

        p = nums[l]
        res = float("inf")

        if p >= target:
            return 1

        for r in range(1, n):
            p += nums[r]
            while p >= target and l <= r:
                p -= nums[l]
                res = min(res, r - l + 1)
                l += 1

        return res if res != float("inf") else 0

