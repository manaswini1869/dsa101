from typing import List
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])

        top, bottom, left, right = x, x+k-1, y, y+k
        while top < bottom:
            grid[top][left:right], grid[bottom][left:right] = grid[bottom][left:right], grid[top][left:right]
            top += 1
            bottom -= 1
        return grid




        