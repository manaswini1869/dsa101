class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        res,x = 0, abs(x)
        while x:
            reminder = x % 10
            res = res * 10 + reminder
            x = x // 10
            if res > 2**31 - 1:
                return 0
        return res * sign