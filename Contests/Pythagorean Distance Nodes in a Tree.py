from typing import List
from collections import deque
class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:

        adj_matrix = [[]*n for _ in range(n)]

        special_nodes = 0

        for u, v in edges:
            adj_matrix[u].append(v)
            adj_matrix[v].append(u)

        def cal_distance(src):
            dist = [float("inf")] * n
            dist[src] = 0
            q = deque([src])
            while q:
                node = q.popleft()
                for nei in adj_matrix[node]:
                    if dist[nei] == float("inf"):
                        dist[nei] = dist[node]+1
                        q.append(nei)
            return dist
        dx = cal_distance(x)
        dy = cal_distance(y)
        dz = cal_distance(z)

        for u in range(n):
            cx, cy, cz = dx[u], dy[u], dz[u]
            if cx**2 + cy**2 == cz**2 or cy**2 + cz**2 == cx**2 or cz**2 + cx**2 == cy**2:
                special_nodes += 1
        return special_nodes




        