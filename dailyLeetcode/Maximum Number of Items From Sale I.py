class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        ans = [0]*(budget+1)
        values = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    cnt += 1
            values.append(1+cnt)

        for i in range(n):
            p = items[i][1]
            val = values[i]
            for c in range(budget, p-1, -1):
                ans[c] = max(ans[c], ans[c-p]+val)

        min_price = min(p for _, p in items)

        for c in range(min_price, budget+1):
            ans[c] = max(ans[c], ans[c-min_price] + 1)



        return ans[budget]
