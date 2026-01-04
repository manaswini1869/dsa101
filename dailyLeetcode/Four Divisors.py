class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        for num in nums:
            curr = num + 1  # 1 + num
            v = set()

            for i in range(2, isqrt(num) + 1):
                if len(v) < 3 and num % i == 0:
                    v.add(i)
                    v.add(num // i)
                elif num % i == 0 and len(v) >= 3:
                    break

            if len(v) == 2:  # exactly two non-trivial divisors
                ans += curr
                ans += sum(v)

        return ans