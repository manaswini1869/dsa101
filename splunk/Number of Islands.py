class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])

        seen = set()
        count = 0

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0" or (r, c) in seen:
                return
            seen.add((r, c))
            # grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count




