from collections import deque
from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def can_cross(day: int) -> bool:
            # build grid
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1  # flood

            queue = deque()
            visited = set()

            # start from all land cells in top row
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    visited.add((0, c))

            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col:
                        if grid[nr][nc] == 0 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))

            return False

        left, right = 0, len(cells)
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
