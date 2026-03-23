from typing import List
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        MOD = 10**9+7
        dp = [[[grid[0][0]]*2 for _ in range(cols)] for _ in range(rows)]

        for r in range(1, rows):
            prev = dp[r-1][0][0]
            curr = grid[r][0]
            dp[r][0][0] = prev*curr
            dp[r][0][1] = prev*curr
        
        for c in range(1, cols):
            prev = dp[0][c-1][0]
            curr = grid[0][c]
            dp[0][c][0] = prev*curr
            dp[0][c][1] = prev*curr
        
        for row in range(1, rows):
            for col in range(1, cols):
                current_value = grid[row][col]
                if current_value >= 0:
                    min_from_above = dp[row - 1][col][0]
                    min_from_left = dp[row][col - 1][0]
                    dp[row][col][0] = min(min_from_above, min_from_left) * current_value
                  
                    max_from_above = dp[row - 1][col][1]
                    max_from_left = dp[row][col - 1][1]
                    dp[row][col][1] = max(max_from_above, max_from_left) * current_value
                
                else:
                    max_from_above = dp[row - 1][col][1]
                    max_from_left = dp[row][col - 1][1]
                    dp[row][col][0] = max(max_from_above, max_from_left) * current_value

                    min_from_above = dp[row - 1][col][0]
                    min_from_left = dp[row][col - 1][0]
                    dp[row][col][1] = min(min_from_above, min_from_left) * current_value


        max_product = dp[-1][-1][1]
        return -1 if max_product < 0 else max_product%MOD



        