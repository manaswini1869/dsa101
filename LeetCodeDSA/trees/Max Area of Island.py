class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        final_area, curr_area = 0, 0

        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols:
                return 0
            if (r, c) in visit or grid[r][c] == 0:
                return 0

            visit.add((r, c))
            grid[r][c] = 0

            area = 1
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visit:
                    curr_area = dfs(i, j)
                    final_area = max(final_area, curr_area)


        return final_area









