class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        no_islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if(r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or
            (r, c) in visited):
                return
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    no_islands += 1

        return no_islands
