class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        cols = len(grid) - 1
        rows = len(grid[0]) - 1

        if grid[cols][rows] != 0 or grid[0][0] != 0:
            return -1

        directions = [(-1,-1),(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def get_neighbours(row, col):
            for row_diff, col_diff in directions:
                new_row = row + row_diff
                new_col = col + col_diff

                if not (0 <= new_row <= rows and 0 <= new_col <= cols):
                    continue
                if grid[new_row][new_col] != 0:
                    continue

                yield (new_row, new_col)



        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (rows, cols):
                return distance

            for nei_row, nei_col in get_neighbours(row, col):
                grid[nei_row][nei_col] = distance + 1

                queue.append((nei_row, nei_col))


        return -1
