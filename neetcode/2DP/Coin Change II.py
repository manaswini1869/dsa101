class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]

        # dp = [0] * (amount + 1)
        # dp[0] = 1  # base case: one way to make 0

        # for coin in coins:
        #     for j in range(coin, amount + 1):
        #         dp[j] += dp[j - coin]

        # return dp[amount]
        # res = 0
        # dp = {} # saving the coin, amount : unique_path so far

        # def dfs(coin_index, collected_amount):
        #     if collected_amount == amount:
        #         return 1
        #     if collected_amount > amount:
        #         return 0
        #     if coin_index >= len(coins):
        #         return 0
        #     if (coin_index, collected_amount) in  dp:
        #         return dp[(coin_index , collected_amount)]

        #     take = dfs(coin_index, collected_amount + coins[coin_index])
        #     skip = dfs(coin_index + 1, collected_amount)

        #     dp[(coin_index, collected_amount)] = take + skip

        #     return dp[(coin_index, collected_amount)]

        # return dfs(0, 0)




