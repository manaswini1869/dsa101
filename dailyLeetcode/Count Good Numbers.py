class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9 + 7)
        noEven, noOdd = 0, 0
        if n % 2 == 0:
            noEven, noOdd = n //2, n//2
        else:
            noEven, noOdd = n//2 + 1, n//2
        count = pow(5, noEven, MOD) * pow(4,noOdd, MOD)
        return count % MOD
