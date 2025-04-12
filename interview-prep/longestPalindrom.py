class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = {}
        longestPalindrome = 0
        for i in s:
            res[ord(i)] = res.get(ord(i), 0) + 1
        for n in res.values():
            longestPalindrome += (n // 2) * 2
            if n % 2 == 1 and longestPalindrome % 2 == 0:
                longestPalindrome += 1
        return longestPalindrome
