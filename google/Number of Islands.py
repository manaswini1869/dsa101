class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()

        count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in seen or grid[r][c] == '0':
                return
            seen.add((r, c))
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)
            return


        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count







