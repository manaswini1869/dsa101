class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])

        min_heap = []
        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    heappush(min_heap, (heightMap[r][c], r, c)) # height value, coordinates (r, c)
                    heightMap[r][c] = -1 # marking it as visited

        res = 0
        max_h = -1
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while min_heap:
            h, r, c = heapq.heappop(min_heap)
            max_h = max(max_h, h)
            res += max_h - h
            for x, y in neighbours:
                if r + x >= rows or c + y >= cols or r + x < 0 or c + y < 0 or heightMap[r+x][c+y] == -1:
                    continue

                heapq.heappush(min_heap, (heightMap[r+x][c+y], r+x, c+y))
                heightMap[r+x][c+y] = -1

        return res






