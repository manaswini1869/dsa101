class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy
        # n = len(nums)
        # goal = n - 1
        # for i in range(n-2, -1, -1):
        #     for j in range(1, nums[i]+1):
        #         if i + j >= goal:
        #             goal = i
        # return goal == 0

        # dp bottom - up
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            max_jump = min(i + nums[i], n-1)
            for j in range(i+1, max_jump+1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]

