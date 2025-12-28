class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        count = 0
        for r in range(rows):
            curr_count = 0
            left, right = 0, cols-1
            if grid[r][left] < 0:
                curr_count = cols
            else:
                while left <= right:
                    mid = (left+right) // 2
                    if grid[r][mid] >= 0:
                        left = mid + 1
                    else:
                        curr_count = cols - mid
                        right = mid - 1
            count += curr_count
        return count






