class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {num: i for i, num in enumerate(arr)}
        dp = {}
        max_length = 0
        for j in range(len(arr)):
            for i in range(j):
                k = index.get(arr[j] - arr[i])
                if k is not None and k < i:
                    dp[i, j] = dp.get((k,i), 2) + 1
                    max_length = max(max_length, dp[i, j])
        print(dp)
        return max_length if max_length >= 3 else 0
