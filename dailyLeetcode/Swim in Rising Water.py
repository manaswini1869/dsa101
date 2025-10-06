class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()

        min_heap = [[grid[0][0], 0, 0]]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == n-1 and c == n-1:
                return t

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visit:
                    heapq.heappush(min_heap, (max(t, grid[nr][nc]), nr, nc))
                    visit.add((nr, nc))




