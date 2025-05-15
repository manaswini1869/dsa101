class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [0] * 26
        for ch in s:
            dp[ord(ch) - ord('a')] += 1
        for _ in range(t):
            new_dp = [0] * 26
            for i in range(26):
                count = dp[i]
                if count == 0:
                    continue
                steps = nums[i]
                for j in range(1, steps+1):
                    next_char = (i+j) % 26
                    new_dp[next_char] = (new_dp[next_char] + count) % MOD
            dp = new_dp
        return sum(dp) % MOD