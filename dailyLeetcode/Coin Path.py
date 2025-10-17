class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        if coins[-1] == -1:
            return []

        n = len(coins)

        path = []

        dp = [float("inf")]*n

        dp[-1] = coins[-1]

        for i in range(n-2, -1, -1):
            if coins[i] != -1:
                for j in range(i+1, min(n, i + maxJump + 1)):
                    if dp[i] > dp[j] + coins[i]:
                        dp[i] = dp[j] + coins[i]
        if dp[0] == float("inf"):
            return []
        s = dp[0]
        for i in range(n):
            if dp[i] == s:
                s -= coins[i]
                path.append(i+1)
        return path






