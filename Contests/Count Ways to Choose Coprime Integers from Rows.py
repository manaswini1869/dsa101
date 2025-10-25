from math import gcd

class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        m = len(mat)

        MOD = 10**9 + 7

        @lru_cache(None)
        def recur(idx, g):
            if idx == m:
                return 1 if g == 1 else 0

            total = 0

            for val in mat[idx]:
                if idx == 0:
                    new_g = val
                else:
                    new_g = gcd(g, val)
                total = (total + recur(idx + 1, new_g)) % MOD

            return total

        return recur(0, 0)


