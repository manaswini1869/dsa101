from typing import List
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        rows, cols = len(grid), len(grid[0])
        arr = []
        for i in range(rows):
            for j in range(cols):
                arr.append(grid[i][j])

        n = len(arr)
        MOD = 12345
        prefix = [1]*n
        for i in range(1, n):
            prefix[i] = (prefix[i-1]*arr[i-1])%MOD
        suffix = [1]*n
        for i in range(n-2, -1, -1):
            suffix[i] = (suffix[i+1]*arr[i+1])%MOD
        res = [[0]*cols for _ in range(rows)]
        for i in range(n):
            p = (prefix[i]*suffix[i])%MOD
            r, c = divmod(i, cols)
            res[r][c] = p
        
        return res

        # rows, cols = len(grid), len(grid[0])
        # full_prod = 1
        # zero = False
        # MOD = 12345
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 0:
        #             zero = True
        #             continue
        #         full_prod *= grid[i][j]
        
        # p = [[1]*cols for _ in range(rows)]
        # for i in range(rows):
        #     for j in range(cols):
        #         if zero:
        #             p[i][j] = 0
        #         else:
        #             p[i][j] = (full_prod // grid[i][j]) % MOD
        # return p



        