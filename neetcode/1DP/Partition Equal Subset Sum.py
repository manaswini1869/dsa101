class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = sum(nums)
        n = len(nums)

        if m % 2 != 0:
            return False

        m = m // 2
        dp = [False] * (m+1)
        dp[0] = True

        for num in nums:
            for s in range(m, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True


        return dp[m]



