class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        buy = prices[0]

        for i in range(1, n):
            profit = max(profit, prices[i]-buy)

            if prices[i] < buy:
                buy = prices[i]

        return profit




