class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)

        n1 = len(word1)
        n2 = len(word2)
        # cols = n2, rows = n1
        dp = [[float("-inf")] * (n2+1) for _ in range(n1+1)]
        for i in range(n2+1):
            dp[n1][i] = n2 - i

        for i in range(n1+1):
            dp[i][n2] = n1 - i

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        return dp[0][0]

