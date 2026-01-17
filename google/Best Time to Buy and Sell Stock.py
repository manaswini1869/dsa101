class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = float("-inf")
        n = len(prices)
        buy_day = 0
        buy_price = float("inf")
        for i in range(n):
            if i > buy_day:
                max_profit = max(max_profit, prices[i]-buy_price)
            if buy_price > prices[i]:
                buy_day = i
                buy_price = prices[i]
        return max_profit if max_profit > 0 else 0



