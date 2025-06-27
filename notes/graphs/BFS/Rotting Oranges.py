class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        res = 0 # time lapsed
        row = len(grid)
        col = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        seen = set()
        count = 0 # fresh oranges
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        if count == 0: # no fresh orange
            return 0

        if not queue and count > 0:
            return -1

        while queue:

            x, y, current_time = queue.popleft()
            res = max(res, current_time)
            for dx, dy in directions:
                new_x, new_y = x+dx, y+dy

                if 0 <= new_x < row  and 0 <= new_y < col:
                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        count -= 1
                        queue.append((new_x, new_y, current_time + 1))

            if count == 0:
                return res + 1

        return -1


