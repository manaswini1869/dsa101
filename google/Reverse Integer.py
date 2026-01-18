class Solution:
    def reverse(self, x: int) -> int:

        ans = 0
        neg = False
        if x < 0:
            neg = True
            x *= -1

        while x:
            rem = x % 10
            ans = ans * 10 + rem
            if ans > 2**31:
                return 0
            x = x//10

        if neg:
            return -1*ans
        return ans







