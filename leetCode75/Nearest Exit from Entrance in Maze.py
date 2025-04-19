from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0], entrance[1], 0))  # (row, col, steps)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            x, y, steps = queue.popleft()

            # Check if this is an exit
            if (x == 0 or y == 0 or x == rows - 1 or y == cols - 1) and [x, y] != entrance:
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == "." and (nx, ny) not in visited:
                    queue.append((nx, ny, steps + 1))
                    visited.add((nx, ny))

        return -1  # No exit found
