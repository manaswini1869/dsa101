class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        # def filler(r, c):
        #     for i in range(m):
        #         if grid[i][c] == 'W':
        #             if i < r:
        #                 continue
        #             else:
        #                 return
        #         grid[i][c] = "G"
        #     for i in range(n):
        #         if grid[r][i] == "W":
        #             if i < c:
        #                 continue
        #             else:
        #                 return
        #         grid[r][i] = "G"
        #     return

        grid = [[0 for _ in range(n)] for _ in range(m)]

        for r, c in walls:
            grid[r][c] = 1

        for r, c in guards:
            grid[r][c] = 2

        directions = [(0, 1), (0,-1), (1,0),(-1,0)]

        for r, c in guards:
            for dr, dc in directions:
                r1 = r + dr
                c1 = c + dc
                while 0 <= r1 < m and 0 <= c1 < n:
                    if grid[r1][c1] in (1, 2):
                        break
                    if grid[r1][c1] == 0:
                        grid[r1][c1] = 3
                    r1 += dr
                    c1 += dc

        return sum(cell == 0 for row in grid for cell in row)





