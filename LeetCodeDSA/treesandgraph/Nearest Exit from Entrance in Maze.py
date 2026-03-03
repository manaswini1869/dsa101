from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        rows, cols = len(maze), len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set([(entrance[0], entrance[1])])

        while q:

            for _ in range(len(q)):
                r, c, curr_steps = q.popleft()
                if curr_steps > 0 and (r==0 or c == 0 or r == rows-1 or c == cols-1):
                    return curr_steps
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in seen or maze[nr][nc] == '+':
                        continue

                    q.append((nr, nc, curr_steps+1))
                    seen.add((nr, nc))





        return -1






