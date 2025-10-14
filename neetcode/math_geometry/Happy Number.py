class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            total = 0
            while n:
                rem = n % 10
                total += rem*rem
                n = n // 10
            n = total
        return False