class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        maxLen = 0
        for i in range(len(s)):
            if s[i] in dic:
                maxLen = max(maxLen, dic[s[i]] + 1)
            dic[s[i]] = i
            res = max(res, i - maxLen + 1)
        return res