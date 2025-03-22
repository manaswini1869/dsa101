class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, cols = len(grid), len(grid[0])
        num_islands = 0
        def dfs(grid, r, c):
            if r < 0 or c < 0 or r>= row or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = "0"
            dfs(grid, r, c+1)
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c-1)
        for i in range(row):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    num_islands += 1
        print(grid)
        return num_islands