# class Solution:
#     def distributeCandies(self, n: int, limit: int) -> int:
#         no_ways = 0
#         no_children = 3
#         for i in range(0, n+1):
#             if i <= limit:
#                 req = n - i
#                 for j in range(0, req+1):
#                     if j <= limit:
#                         for k in range(0, req+1):
#                             if k <= limit:
#                                 if i+j+k == n:
#                                     no_ways += 1
#         return no_ways

# import math

# class Solution:
#     def distributeCandies(self, n: int, limit: int) -> int:
#         def nCk(n, k):
#             if k < 0 or k > n:
#                 return 0
#             return math.comb(n, k)

#         # Number of integer solutions to x + y + z = n
#         # where each of x, y, z ∈ [0, limit]
#         res = 0
#         for i in range(0, 4):  # up to 3 variables, so 0 to 3 inclusive
#             sign = (-1)**i
#             res += sign * nCk(3, i) * nCk(n - i * (limit + 1) + 2, 2)
#         return res

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit, n)+1):
            if n - i > 2*limit:
                continue
            ans += min(n-i, limit) - max(0, n-i-limit) + 1
        return ans

