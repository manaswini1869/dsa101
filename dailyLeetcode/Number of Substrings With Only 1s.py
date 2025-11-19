class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0

        while i < n:
            if s[i] == '1':
                j = i
                while j < n and s[j] == '1':
                    j += 1
                count = j - i
                res += (count * (count + 1)) // 2
                i = j
            else:
                i += 1

        # for i in range(n):
        #     if s[i] == '1':
        #         for j in range(i, n):
        #             if s[j] == '1':
        #                 res += 1
        #             else:
        #                 break
        return res % (10**9 + 7)
