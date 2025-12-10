class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        res = float("-inf")
        curr_buy = prices[0]
        for i, pr in enumerate(prices[1:]):
            curr_profit = (pr - curr_buy)
            res = max(res, curr_profit)
            curr_buy = min(curr_buy, pr)


        return res if res > 0 else 0


