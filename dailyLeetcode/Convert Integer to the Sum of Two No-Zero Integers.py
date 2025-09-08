class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n % 2 == 0:
            a, b = n // 2, n // 2
        else:
            a, b = n // 2, n // 2 + 1
        while '0' in str(a) or '0' in str(b):
                a, b = a - 1, b + 1

        return [a, b]