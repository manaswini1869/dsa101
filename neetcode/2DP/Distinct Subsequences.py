class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n1 = len(s)
        n2 = len(t)

        res = 0
        # memo = {}

        # def dfs(i, j):
        #     if j == n2:
        #         return 1
        #     if i == n1:
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     res = dfs(i+1, j)

        #     if s[i] == t[j]:
        #         res += dfs(i+1, j+1)
        #     memo[(i, j)] = res
        #     return res

        # return dfs(0, 0)

        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][n2] = 1

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                dp[i][j] = dp[i+1][j]

                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]

        return dp[0][0]