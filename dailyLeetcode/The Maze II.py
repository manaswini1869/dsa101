from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        q = deque()
        q.append((start[0], start[1]))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(maze), len(maze[0])

        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[start[0]][start[1]] = 0

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni, nj = i, j
                steps = 0

                # roll correctly
                while 0 <= ni + di < rows and 0 <= nj + dj < cols and maze[ni + di][nj + dj] == 0:
                    ni += di
                    nj += dj
                    steps += 1

                if dist[i][j] + steps < dist[ni][nj]:
                    dist[ni][nj] = dist[i][j] + steps
                    q.append((ni, nj))

        res = dist[destination[0]][destination[1]]
        return res if res != float("inf") else -1
