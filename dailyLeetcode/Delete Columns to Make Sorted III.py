class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        rows, cols = len(strs), len(strs[0])

        dp = [1]*cols

        for j in range(cols):
            for i in range(j):
                if all(strs[r][i] <= strs[r][j] for r in range(rows)):
                    dp[j] = max(dp[j], dp[i]+1)




        return cols - max(dp)



