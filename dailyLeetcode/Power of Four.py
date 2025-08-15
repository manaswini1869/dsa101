class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            n = n / 4

        return n == 1
        # if n < 0:
        #     return False
        # i = 0
        # while True:
        #     tmp = 4 ** i
        #     if n == tmp:
        #         return True
        #     elif tmp > n:
        #         return False
        #     i += 1
