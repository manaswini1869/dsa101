class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        str1, str2 = {}, {}
        for i in range(len(s)):
            str1[s[i]] = 1 + str1.get(s[i], 0)
            str2[t[i]] = 1 + str2.get(t[i], 0)
        return str1 == str2