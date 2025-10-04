class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_sum = sum(nums)

        if abs(target) > total_sum:
            return 0

        dp = [[0]* (2*total_sum+1) for _ in range(n)]

        dp[0][nums[0] + total_sum] += 1
        dp[0][-nums[0] + total_sum] += 1


        for i in range(1, n):
            for s in range(-total_sum, total_sum+1):
                if dp[i-1][s + total_sum] > 0:
                    dp[i][s+nums[i]+total_sum] += dp[i-1][s+total_sum]
                    dp[i][s-nums[i]+total_sum] += dp[i-1][s+total_sum]

        return dp[n-1][target+total_sum]