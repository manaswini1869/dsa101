class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1+s2) != len(s3):
            return False

        n1 = len(s1)
        n2 = len(s2)

        dp = [[False]*(n2+1) for _ in range(n1+1)]

        dp[n1][n2] = True
        print(dp)
        for i in range(n1, -1, -1):
            for j in range(n2, -1, -1):
                if i < n1 and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < n2 and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True


        return dp[0][0]





        return dp[0][0]