class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k = 2
        rem_count = [[0] * k for _ in range(k)]
        max_len = 0

        for num in nums:
            rem = num % k
            for j in range(k):
                prev_rem = (j - rem + k) % k
                rem_count[rem][prev_rem] = rem_count[prev_rem][rem] + 1
                max_len = max(max_len, rem_count[rem][prev_rem])

        return max_len