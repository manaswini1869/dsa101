class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        n = len(prices)

        prefix = [0]*(n+1)
        profit = [0]*(n+1)

        for i in range(n):
            profit[i+1] = profit[i] + (prices[i]*strategy[i])
            prefix[i+1] = prefix[i] + prices[i]


        res = profit[n]
        for i in range(k-1, n):
            left = profit[i-k+1]
            right = profit[n] - profit[i+1]
            change = prefix[i+1] - prefix[i-k//2+1]
            res = max(res, left+right+change)
        return res




        # n = len(prices)
        # original = 0

        # for i in range(n):
        #     original += (prices[i]*strategy[i])

        # final = float("-inf")
        # final = max(final, original)
        # for i in range(n):
        #     original = 0
        #     temp = strategy[:]
        #     if i + k <= n:
        #         for m in range(i, i+k//2):
        #             temp[m] = 0
        #         for m in range(i+k//2, i+k):
        #             temp[m] = 1
        #     for j in range(n):
        #         original += (prices[j]*temp[j])

        #     final = max(final, original)

        # return final








