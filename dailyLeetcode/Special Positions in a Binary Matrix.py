from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        rows, cols = len(mat), len(mat[0])
        count = 0
        row_count = [sum(row) for row in mat]
        col_count = [sum(mat[i][j] for i in range(rows)) for j in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j]==1:
                    count += 1
        return count
    # time complexity : O(rols*cols)
    # space complexity : O(rols+cols)



        