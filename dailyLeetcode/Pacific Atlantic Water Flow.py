class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific_min_heap = []
        atlantic_min_heap = []

        result = []

        for j in range(cols):
            pacific_min_heap.append((0,j))
            atlantic_min_heap.append((rows-1,j))

        for j in range(rows):
            pacific_min_heap.append((j,0))
            atlantic_min_heap.append((j,cols-1))

        pacific_loop = set()
        atlantic_loop = set()

        def bfs(start):
            queue = deque(start)
            visited = set()
            for r, c in start:
                visited.add((r, c))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[r][c] <= heights[nr][nc]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        pacific_loop = bfs(pacific_min_heap)
        atlantic_loop = bfs(atlantic_min_heap)
        result = [list(cell) for cell in pacific_loop & atlantic_loop]


        return result
