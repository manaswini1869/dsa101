class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # canBuy = True
        # max_profit = float("-inf")
        # n = len(prices)
        # min_price = float("inf")
        # for price in prices:
        #     min_price = min(min_price, price)
        #     max_profit = max(max_profit, price - min_price)

        # return max_profit

        dp = {} # (index, canBuy) : profit

        def dfs(i, canBuy):
            if i >= len(prices):
                return 0

            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            cooldown = dfs(i+1, canBuy)

            # when buying
            if canBuy:
                buy = dfs(i+1, not canBuy) - prices[i]
                dp[(i, canBuy)] = max(buy, cooldown)
            # when selling
            else:
                sell = dfs(i+2, not canBuy) + prices[i]
                dp[(i, canBuy)] = max(sell, cooldown)

            return dp[(i, canBuy)]

        return dfs(0, True)






