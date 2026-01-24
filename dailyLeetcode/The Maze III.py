class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:

        rows, cols = len(maze), len(maze[0])

        directions = {'d':(1, 0),'l':(0, -1), 'r':(0, 1), 'u':(-1, 0)}
        q = []
        heapq.heappush(q, (0, "", ball[0], ball[1]))
        dist = [[(float("inf"), "") for _ in range(cols)] for _ in range(rows)]
        dist[ball[0]][ball[1]] = (0, "")

        while q:
            d, path, r, c = heapq.heappop(q)
            if [r, c] == hole:
                return path
            if (d, path) > dist[r][c]:
                continue

            for m, (dr, dc) in directions.items():
                nr, nc = r, c
                steps = 0
                while 0 <= nr+dr < rows and 0 <= nc + dc < cols and maze[nr+dr][nc+dc] == 0:
                    steps += 1
                    nr += dr
                    nc += dc
                    if [nr, nc] == hole:
                        break
                new_dist = d + steps
                new_path = path + m
                if (new_dist, new_path) < dist[nr][nc]:
                    dist[nr][nc] = (new_dist, new_path)
                    heapq.heappush(q, (new_dist, new_path, nr, nc))

        return "impossible"











