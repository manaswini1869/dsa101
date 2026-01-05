class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        max_sum = 0
        min_neg = float("inf")
        count = 0
        for i in range(n):
            for j in range(n):
                max_sum += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    count += 1
                min_neg = min(min_neg, abs(matrix[i][j]))

        if count % 2 == 0:
            return max_sum

        return max_sum - 2*min_neg


