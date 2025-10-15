class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)

        # for i in range(n+1):
        #     count = 0
        #     while i:
        #         count += 1 if 1 & i else 0
        #         i >>= 1
        #     res.append(count)
        # return res

        for i in range(n+1):
            res[i] = res[i >> 1] + (1&i)

        return res