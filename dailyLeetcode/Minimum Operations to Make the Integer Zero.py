class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            diff = num1 - k * num2
            if diff < 0:
                continue
            if diff >= k and bin(diff).count("1") <= k:
                return k
        return -1