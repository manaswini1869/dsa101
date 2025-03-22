class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for i in range(1, len(row) - 1):
                row[i] = res[row_num - 1][i - 1] + res[row_num - 1][i]
            res.append(row)

        return res