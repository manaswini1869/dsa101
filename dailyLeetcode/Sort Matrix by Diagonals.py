class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        # rows, cols = len(grid), len(grid[0])

        # res = [[0]*cols for _ in range(rows)]

        # for d in range(cols + rows - 1):

        #     if d < rows:
        #         r, c = rows - d -1, 0
        #     else:
        #         r, c = 0, d - cols + 1

        #     diagonal = []
        #     rr, cc = r, c
        #     while r < rows and c < cols:
        #         diagonal.append(grid[r][c])
        #         r += 1
        #         c += 1
        #     dia = sorted(diagonal)
        #     if d < rows:
        #         dia = dia[::-1]

        #     i = 0
        #     while rr < rows and cc < cols:
        #         res[rr][cc] = dia[i]
        #         rr += 1
        #         cc += 1
        #         i += 1

        # return res
        n = len(grid)

        for i in range(n):
            tmp = [grid[i+j][j] for j in range(n-i)]
            tmp.sort(reverse=True)
            for j in range(n-i):
                grid[i+j][j] = tmp[j]

        for j in range(1, n):
            tmp = [grid[i][j + i] for i in range(n - j)]
            tmp.sort()
            for i in range(n - j):
                grid[i][j + i] = tmp[i]

        return grid