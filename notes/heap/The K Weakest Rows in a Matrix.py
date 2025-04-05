class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_sol_row = []
        res = []
        for row in range(len(mat)):
            num_sol_row.append((sum(mat[row]), row))
        num_sol_row.sort()
        print(num_sol_row)
        res = []
        for i in range(k):
            res.append(num_sol_row[i][1])
        return res