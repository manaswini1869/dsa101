from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened_grid = [num for row in grid for num in row]
        flattened_grid.sort()
        base = flattened_grid[0]
        for num in flattened_grid:
            if (num - base) % x != 0:
                return -1
        n = len(flattened_grid)
        median = flattened_grid[n // 2]
        operations = sum(abs(num - median) // x for num in flattened_grid)

        return operations
