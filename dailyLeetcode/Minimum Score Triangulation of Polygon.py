from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @cache
        def dfs(i, j):
            if i+1 == j:
                return 0

            min_score = float("inf")
            for k in range(i+1, j):
                curr = dfs(i, k) + dfs(k, j) + values[i]*values[k]*values[j]

                min_score = min(min_score, curr)

            return min_score

        return dfs(0, len(values)-1)

