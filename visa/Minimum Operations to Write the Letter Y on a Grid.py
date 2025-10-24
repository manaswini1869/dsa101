class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        y_count = {}
        o_count = {}
        k = n - 1
        for i in range(n):
            for j in range(n):
                if i >= n// 2 and j == n // 2:
                    y_count[grid[i][j]] = y_count.get(grid[i][j], 0) + 1
                elif (i == j and i <= n//2):
                    y_count[grid[i][j]] = y_count.get(grid[i][j], 0) + 1
                elif (i+j == n-1 and i <= n // 2):
                    y_count[grid[i][j]] = y_count.get(grid[i][j], 0) + 1
                else:
                    o_count[grid[i][j]] = o_count.get(grid[i][j], 0) + 1
        ops = float("inf")
        total_y = sum(y_count.values())
        total_o = sum(o_count.values())

        for y_digit in [0,1,2]:
            for o_digit in [0,1,2]:
                if y_digit == o_digit:
                    continue
                cost = (total_y - y_count.get(y_digit, 0)) + (total_o - o_count.get(o_digit,0))
                ops = min(ops, cost)

        return ops

