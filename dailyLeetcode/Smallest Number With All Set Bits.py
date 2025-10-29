class Solution:
    def smallestNumber(self, n: int) -> int:
        # x = n
        # while x >= n:
        #     if set(str(bin(x))[2:]) == {"1"}:
        #         return x
        #     x += 1

        x = 1
        while x < n:
            x = x*2+1
        return x

