class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visit = set()
        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))
            while q:
                r1, c1 = q.popleft()
                for dr, dc in directions:
                    nr, nc = r1+dr, c1+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit and grid[nr][nc] == "1":
                        visit.add((nr, nc))
                        q.append((nr, nc))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    count += 1

        return count


