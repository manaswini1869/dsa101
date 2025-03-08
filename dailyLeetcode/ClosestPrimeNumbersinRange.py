import math
class Solution:
    def isPrime(self, num):
        if num < 2:
            return False
        if num in (2,3):
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = []
        for num in range(left, right+1):
            if self.isPrime(num):
                primes.append(num)

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        res = [-1, -1]
        for i in range(len(primes)-1):
            if (primes[i+1] - primes[i]) < min_diff:
                min_diff = primes[i+1] - primes[i]
                res = [primes[i], primes[i+1]]
        return res

