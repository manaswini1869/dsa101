class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # visit = [[False for _ in range(cols)] for _ in range(rows)]

        # def dfs(r, c):
        #     if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or visit[r][c]):
        #         return INF
        #     if grid[r][c] == 0:
        #         return 0

        #     visit[r][c] = True
        #     res = INF
        #     for dr, dc in directions:
        #         res = min(res, 1 + dfs(r+dr, c+dc))
        #     visit[r][c] = False
        #     return res

        def bfs(r, c):
            queue = deque([(r, c)])
            visit = [[False for _ in range(cols)] for _ in range(rows)]
            visit[r][c] = True
            steps = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    if grid[r][c] == 0:
                        return steps

                    for dx, dy in directions:
                        if (0 <= r + dx < rows and 0 <= c + dy < cols and
                        not visit[r + dx][c + dy] and grid[r + dx][c + dy] != -1 ):
                            visit[r+dx][c+dy] = True
                            queue.append((r+dx, c+dy))
                steps += 1
            return INF


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)


