class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp bottom-up
        # n = len(nums)
        # dp = [float("inf")] * n
        # dp[n-1] = 0

        # for i in range(n-2, -1, -1):
        #     for j in range(1, nums[i]+1):
        #         if i + j < n:
        #             dp[i] = min(dp[i], dp[i+j] + 1)

        # return dp[0]

        # greedy
        n = len(nums)
        l = r = 0
        res = 0

        while r < n - 1:
            max_jump = 0
            for j in range(l, r+1):
                max_jump = max(max_jump, j + nums[j])

            l = r + 1
            r = max_jump
            res += 1

        return res








