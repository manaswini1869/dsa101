class Solution:
    def maxOperations(self, s: str) -> int:

        ans = 0
        ones = 0

        for i, x in enumerate(s):
            if x == '1':
                ones += 1
            elif i+1 == len(s) or s[i+1] == '1':
                ans += ones

        return ans


