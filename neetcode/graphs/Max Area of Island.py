class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if (r < 0 or r>=rows or c < 0 or c >= cols
            or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            curr_area = 1
            curr_area += dfs(r+1, c)
            curr_area += dfs(r-1, c)
            curr_area += dfs(r, c+1)
            curr_area += dfs(r, c-1)
            return curr_area

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area
