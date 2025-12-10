class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        if amount == 0:
            return 0

        if not n:
            return -1
        if n == 1:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return -1

        dp = [float("inf")] * (amount + 1)

        dp[0] = 0

        for amt in range(1, amount+1):

            for c in coins:
                if (amt - c) >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt-c])
        return dp[amount] if dp[amount] != float("inf") else -1



        # num_coins = 0
        # q = deque()
        # q.append((amount, 0))
        # visited = set([amount])

        # while q:
        #     curr_amt, curr_coin = q.popleft()
        #     for c in coins:
        #         nxt = curr_amt - c
        #         if nxt == 0:
        #             return curr_coin + 1
        #         if nxt not in visited and nxt > 0:
        #             q.append((nxt, curr_coin+1))
        #             visited.add(nxt)

        # return -1




