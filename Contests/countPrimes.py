import math

class Solution:
    def countPrimes(self, n: int) -> int:
        # def is_prime(num):
        #     if num < 2:
        #         return False
        #     for i in range(2, int(math.sqrt(num)) + 1):
        #         if num % i == 0:
        #             return False
        #     return True

        # res = 0
        # for i in range(2, n):
        #     if is_prime(i):
        #         res += 1
        # return res
        if n < 2:
            return 0
        numbers = [False, False] + [True] * (n-2)
        for p in range(2, int(sqrt(n)) + 1):
            if numbers[p]:
                for multiple in range(p*p, n, p):
                    numbers[multiple] = False
        return sum(numbers)
