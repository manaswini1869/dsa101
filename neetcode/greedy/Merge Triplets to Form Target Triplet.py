# class Solution:
#     def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
#         n = len(triplets)
#         a = []
#         b = []
#         c = []

#         for i in range(n):
#             if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
#                 continue
#             a.append(triplets[i][0])
#             b.append(triplets[i][1])
#             c.append(triplets[i][2])

#         if target[0] not in a or target[1] not in b or target[2] not in c:
#             return False

#         return True


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3