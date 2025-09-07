class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0] * 1
        res = []
        if n % 2 == 0:
            lim = n // 2
            for i in range(-1, -lim-1, -1):
                res.append(i)
                res.append(-i)
        else:
            lim = n
            for i in range(1, lim):
                res.append(i)
            res.append(-(sum(res)))
        return res