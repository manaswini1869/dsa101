class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p <= 1:
            return 1
        if p == 2:
            return 6

        MOD = 10**9 + 7

        max_val = 2**p - 1
        second = max_val - 1
        pw = 2**(p-1) - 1

        return (pow(second, pw, MOD) * max_val) % MOD

