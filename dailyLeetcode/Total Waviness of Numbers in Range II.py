from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:

            if n <= 0:
                return 0

            s = str(n)

            @lru_cache(None)
            def dp(pos, prev2, prev1, tight, started):

                if pos == len(s):
                    return (0, 1)

                limit = int(s[pos]) if tight else 9

                total_wavy = 0
                total_count = 0

                for d in range(limit + 1):

                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        wavy, cnt = dp(pos + 1, -1, -1, ntight, False)

                    else:

                        add = 0

                        if prev2 != -1:
                            if (prev2 < prev1 > d) or (prev2 > prev1 < d):
                                add = 1

                        wavy, cnt = dp(pos + 1, prev1, d, ntight, True)

                        wavy += add * cnt

                    total_wavy += wavy
                    total_count += cnt

                return (total_wavy, total_count)

            return dp(0, -1, -1, True, False)[0]

        return solve(num2) - solve(num1 - 1)

# class Solution:
#     def totalWaviness(self, num1: int, num2: int) -> int:

#         res = 0
#         for i in range(num1, num2+1):
#             strnum = str(i)
#             curr = 0
#             for j in range(1, len(strnum)-1):
#                 if (strnum[j-1] < strnum[j] > strnum[j+1]) or (strnum[j-1] > strnum[j] < strnum[j+1]):
#                     curr += 1
#             res += curr
#         return res


        