class Solution:
    def numOfWays(self, n: int) -> int:

        MOD = 10**9+7
        aba_pattern = 6
        abc_pattern = 6

        for ci in range(n-1):
            next_aba_count = (3 * aba_pattern + 2 * abc_pattern) % MOD
            next_abc_count = (2 * aba_pattern + 2 * abc_pattern) % MOD

            aba_pattern = next_aba_count
            abc_pattern = next_abc_count
        return (aba_pattern + abc_pattern)%MOD


