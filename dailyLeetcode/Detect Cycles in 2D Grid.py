from typing import List
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        rows, cols = len(grid), len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):

                if visited[r][c]:
                    continue
                visited[r][c] = True
                stack = [(r, c, -1, -1)]

                while stack:
                    cr, cc, pr, pc = stack.pop()
                    for dr, dc in directions:
                        nr = dr + cr
                        nc = dc + cc

                        if 0 <= nr < rows and 0 <= nc < cols:
                            if (grid[nr][nc] != grid[cr][cc]) or (nr == pr and nc == pc):
                                continue
                            if visited[nr][nc]:
                                return True
                            visited[nr][nc] = True
                            stack.append((nr, nc, cr, cc))
        return False
        