class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        maxl = 0
        curre = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            curre = max(curre, freq[s[r]])
            while(r - maxl + 1) - curre > k:
                freq[s[maxl]] -= 1
                maxl += 1
            res = max(res, r - maxl + 1)
        return res