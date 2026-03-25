from typing import List
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        rows, cols = len(grid), len(grid[0])
        total = 0
        for i in range(rows):
            for j in range(cols):
                total += grid[i][j]
        if total % 2 != 0:
            return False
        curr = 0
        for r in range(rows-1):
            curr += sum(grid[r])
            if curr == (total//2):
                return True
        cols_sum = [0]*cols
        for i in range(rows):
            for j in range(cols):
                cols_sum[j] += grid[i][j]
        
        curr = 0
        for c in range(cols-1):
            curr += cols_sum[c]
            if curr == (total//2):
                return True


        return False
        





