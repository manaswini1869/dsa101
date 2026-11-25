class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        n = len(nums)
        curr = float("inf")

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                length = j - i + 1
                if length > r:
                    break
                if length >= l and s > 0:
                    curr = min(curr, s)

        return -1 if curr == float('inf') else curr