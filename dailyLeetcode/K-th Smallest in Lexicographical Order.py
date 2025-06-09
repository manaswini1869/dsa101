class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # result = []
        # curr = 1
        # while len(result) < n:
        #     result.append(curr)
        #     if len(result) == k:
        #         return result[k-1]
        #     if curr * 10 <= n:
        #         curr *= 10
        #     else:
        #         while curr == n or curr % 10 == 9:
        #             curr //= 10
        #         curr += 1
        curr = 1
        i = 1
        def count(curr):
            res = 0
            nei = curr + 1
            while curr <= n:
                res += min(nei, n+1) - curr
                curr *= 10
                nei *= 10
            return res

        while i < k:
            steps = count(curr)
            if i + steps <= k:
                curr += 1
                i += steps
            else:
                curr *= 10
                i += 1

        return curr