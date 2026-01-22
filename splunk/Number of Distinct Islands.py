class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        shapes = set()

        def dfs(r, c, base_r, base_c, shape):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited):
                return
            visited.add((r, c))
            shape.append((r-base_r, c-base_c))

            dfs(r+1, c, base_r, base_c, shape)
            dfs(r-1, c, base_r, base_c, shape)
            dfs(r, c+1, base_r, base_c, shape)
            dfs(r, c-1, base_r, base_c, shape)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    shape = []
                    dfs(r, c, r, c, shape)
                    shapes.add(tuple(shape))
        return len(shapes)







