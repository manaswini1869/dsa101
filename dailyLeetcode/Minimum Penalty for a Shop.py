class Solution:
    def bestClosingTime(self, customers: str) -> int:

        n = len(customers)
        prefix = [0]*(n+1)
        suffix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (customers[i]=='N')
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] + (customers[i] == 'Y')
        ans = 0
        val = float("inf")
        for i in range(n+1):
            if suffix[i] + prefix[i] < val:
                val = suffix[i]+prefix[i]
                ans = i


        return ans








