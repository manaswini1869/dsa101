from collections import defaultdict, deque
from typing import List

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(matrix), len(matrix[0])

        teleport = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j].isalpha():
                    teleport[matrix[i][j]].append((i, j))

        q = deque([(0, 0)])
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0

        while q:
            r, c = q.popleft()
            moves = dist[r][c]
            if r == rows - 1 and c == cols - 1:
                return moves

            ch = matrix[r][c]
            if ch.isalpha() and ch in teleport:
                for tr, tc in teleport[ch]:
                    if (tr, tc) != (r, c) and moves < dist[tr][tc]:
                        dist[tr][tc] = moves
                        q.appendleft((tr, tc))
                del teleport[ch]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != '#' and moves + 1 < dist[nr][nc]:
                    dist[nr][nc] = moves + 1
                    q.append((nr, nc))


        return -1
