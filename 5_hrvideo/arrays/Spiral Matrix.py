class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])
        res = []

        top, bottom = 0, m-1
        left, right = 0, n-1

        while top <= bottom and left <= right:

            for c in range(left, right+1):
                res.append(matrix[top][c])
            top += 1
            for c in range(top, bottom+1):
                res.append(matrix[c][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left-1, -1):
                    res.append(matrix[bottom][c])

                bottom -= 1
            if left <= right:
                for c in range(bottom, top-1, -1):
                    res.append(matrix[c][left])
                left += 1

        return res



