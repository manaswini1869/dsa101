class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        n = 1
        length = 1

        for _ in range(1, k+1):
            if n % k == 0:
                return length
            n = n*10 + 1
            length += 1

        return -1
