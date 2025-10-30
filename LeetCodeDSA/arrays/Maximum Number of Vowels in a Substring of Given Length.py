class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        curr_count = 0

        for l in s[:k]:
            if l in vowels:
                curr_count += 1

        l = 0
        n = len(s)
        res = curr_count
        for r in range(k, n):
            if s[l] in vowels:
                curr_count -= 1
            l += 1
            if s[r] in vowels:
                curr_count += 1
            res = max(res, curr_count)

        return res

