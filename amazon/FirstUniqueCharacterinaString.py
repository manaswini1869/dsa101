class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = {} # contain character and string
        for i in range(len(s)):
            res[s[i]] = res.get(s[i], 0) + 1
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i
        return -1
