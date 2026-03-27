class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows, cols = len(mat), len(mat[0])
        k %= cols

        for r in range(rows):
            for c in range(cols):
                if r % 2 == 0:
                    new_c = (c + k) % cols
                else:
                    new_c = (c - k) % cols

                if mat[r][c] != mat[r][new_c]:
                    return False

        return True

# class Solution:
#     def areSimilar(self, mat: List[List[int]], k: int) -> bool:
#         rows, cols = len(mat), len(mat[0])
#         k %= cols

#         if not k:
#             return True
#         for r in range(rows):
#             row = mat[r][(-1) ** (r) * k:] + mat[r][:(-1) ** (r) * k]
#             if row != mat[r]:
#                 return False

#         return True