class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        left = 0

        curr = 0
        res = float("inf")

        for right in range(n):
            curr += nums[right]

            while curr >= target:
                res = min(res, right - left + 1)
                curr -= nums[left]
                left += 1

        return res if res != float("inf") else 0





