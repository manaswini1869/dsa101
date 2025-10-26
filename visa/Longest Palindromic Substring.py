class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if not s:
        #     return ""
        # n = len(s)
        # ans = ""
        # for i in range(n):
        #     for j in range(i, n):
        #         tmp = s[i:j+1]
        #         if tmp == tmp[::-1] and len(tmp) > len(ans):
        #             ans = tmp
        # return ans


        if not s:
            return ""

        start, end = 0, 0
        n = len(s)

        for i in range(n):
            for j in [0, 1]:
                l, r = i, i+j
                while l >= 0 and r < n and s[l] == s[r]:
                    l-=1
                    r+=1
                if r - l - 1 > end - start:
                    start, end = l + 1, r

        return s[start:end]
