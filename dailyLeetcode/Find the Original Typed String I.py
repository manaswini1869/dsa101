class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        n = len(word)
        for i in range(1, n):
            if word[i-1] == word[i]:
                res += 1
        return res
