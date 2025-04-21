# class Solution:
#     def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
#         n = len(differences)
#         hidden = [0]*(n+1)
#         count = 0
#         for i in range(lower, upper + 1):
#             hidden[0] = i
#             for j in range(n):
#                 hidden[j+1] = differences[j] + hidden[j]
#             k = 0
#             for hid in hidden:
#                 if lower <= hid <= upper:
#                     k += 1
#             if k == len(hidden):
#                 count += 1
#         return count
class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        min_prefix = 0
        max_prefix = 0

        for d in differences:
            prefix += d
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)

        return max(0, (upper - lower) - (max_prefix - min_prefix) + 1)
