class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += ((97 - ord(s[i])) + 26) * (i+1)
        return res