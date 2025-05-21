class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # m = len(matrix[0])
        # locations = []
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             locations.append((i, j))
        # for loc in locations:
        #     x, y = loc
        #     for i in range(m):
        #         matrix[x][i] = 0
        #     for j in range(n):
        #         matrix[j][y] = 0
        flag = False
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            if matrix[i][0] == 0:
                flag = True
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, r):
            for j in range(1, c):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(c):
                matrix[0][j] = 0

        if flag:
            for i in range(r):
                matrix[i][0] = 0

