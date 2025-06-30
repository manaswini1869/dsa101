class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        efforts = [[float('inf')]*cols for _ in range(rows)]
        efforts[0][0] = 0

        min_heap = [(0, 0, 0)] # effort, row, col

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            current_effort, row, col = heapq.heappop(min_heap)
            if current_effort > efforts[row][col]:
                continue

            if row == rows - 1 and col == cols - 1:
                return efforts[row][col]

            for x, y in directions:
                new_x, new_y = row + x, col + y
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    to_move = abs(heights[new_x][new_y] - heights[row][col])

                    new_path = max(current_effort, to_move)

                    if new_path < efforts[new_x][new_y]:
                        efforts[new_x][new_y] = new_path
                        heapq.heappush(min_heap, (new_path, new_x, new_y))

        return efforts[rows-1][cols-1]