class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        f = [1]*n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                f[i] = f[i-1] + 1
        g = [1]*n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                g[i] = g[i+1] + 1

        ans = 0
        for i in range(1, n):
            ans = max(ans, min(f[i-1], g[i]))

        return ans