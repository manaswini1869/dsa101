from typing import List
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        rows, cols = len(grid), len(grid[0])

        arr = []
        for i in range(rows):
            for j in range(cols):
                arr.append(grid[i][j])
        n = rows*cols

        rem = arr[0] % x
        for num in arr:
            if num % x != rem:
                return -1

        arr.sort()
        median = arr[n//2]
        return sum(abs(num - median) // x for num in arr)



