class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # n = len(power)
        # count = Counter(power)
        # unique = sorted(count.keys())
        # n = len(unique)

        # @lru_cache(None)
        # def dfs(x):
        #     if x >= n:
        #         return 0

        #     skip = dfs(x + 1)
        #     damage = unique[x]*count[unique[x]]

        #     j = x + 1
        #     while j < n and unique[j] - unique[x] <=2:
        #         j += 1
        #     take = damage + dfs(j)

        #     return max(skip, take)

        # return dfs(0)

        count = Counter(power)
        unique = sorted(count.keys())
        n = len(unique)

        dp = [0]*n

        for i in range(n):
            damage = unique[i] * count[unique[i]]
            if i == 0:
                dp[i] = damage
            else:
                j = i - 1
                while j >= 0 and unique[i] - unique[j] <= 2:
                    j -= 1
                if j >= 0:
                    dp[i] = max(dp[i-1], damage + dp[j])
                else:
                    dp[i] = max(dp[i-1], damage)

        return dp[-1]


