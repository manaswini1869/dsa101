class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        k = len(queries)
        res = [0] * k
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])

        heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))

        count = 0
        index = 0

        while index < k:
            query_index, query_value = sorted_queries[index]

            while heap and heap[0][0] < query_value:
                value, x, y = heappop(heap)
                count += 1

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        heappush(heap, (grid[nx][ny], nx, ny))
                        visited.add((nx, ny))
            res[query_index] = count
            index += 1
        return res

