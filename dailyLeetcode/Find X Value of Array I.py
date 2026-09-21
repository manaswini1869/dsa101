class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:

        rows = len(nums)


        dp = [[0]*k for _ in range(rows)]

        for i in range(rows):
            dp[i][nums[i] % k] += 1

            if i == 0:
                continue

            for r in range(k):
                dp[i][(r*nums[i]) % k] += dp[i-1][r]
        
        res = [0]*k
        for i in range(rows):
            for j in range(k):
                res[j] += dp[i][j]
        

        return res



        