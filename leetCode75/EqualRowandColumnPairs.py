class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        row_count = {}
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_count:
                row_count[row_tuple] += 1
            else:
                row_count[row_tuple] = 1
        n = len(grid)
        for i in range(n):
            col_tuple = tuple(grid[j][i] for j in range(n))
            print(col_tuple)
            if col_tuple in row_count:
                count += row_count[col_tuple]
        print(row_count)
        return count