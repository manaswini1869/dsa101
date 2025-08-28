class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        x1, x2, y1, y2 = float('inf'), float('-inf'), float('inf'), float('-inf')
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    x1 = min(x1, i)
                    x2 = max(x2, i)
                    y1 = min(y1, j)
                    y2 = max(y2, j)

        return (x2 - x1 + 1) * (y2 - y1 + 1)