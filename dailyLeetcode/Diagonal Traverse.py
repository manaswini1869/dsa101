class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])

        res = []

        for d in range(rows + cols - 1):
            if d < cols:
                r, c = 0, d
            else:
                r, c = d - cols + 1, cols - 1

            diagonal = []
            while r < rows and c >= 0:
                diagonal.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                diagonal[::-1]

            res.extend(diagonal)


        return res