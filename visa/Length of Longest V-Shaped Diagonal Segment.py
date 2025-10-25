class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        result = 0

        dirs = [(1,1), (1,-1), (-1,-1), (-1,1)]
        @cache
        def dfs(x, y, direction, turn, target):
            nx, ny = x + dirs[direction][0], y + dirs[direction][1]

            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != target:
                return 0
            turn_int = 1 if target else 0

            max_step = dfs(nx, ny, direction, turn, 2 - target)

            if turn:
                max_step = max(max_step, dfs(nx, ny, (direction+1) % 4, False, 2 - target))
            return max_step+1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for direction in range(4):
                        result = max(result, dfs(i, j, direction, True, 2) + 1)

        return result

