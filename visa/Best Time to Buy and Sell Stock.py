class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy = prices[0]

        n = len(prices)

        for right in range(1, n):
            if prices[right] < buy:
                buy = prices[right]
            else:
                profit = max(profit, prices[right] - buy)

        return profit


