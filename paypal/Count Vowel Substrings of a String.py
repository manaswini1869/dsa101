class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        res = {v:0 for v in vowels}
        number = 0
        n = len(word)

        left, right = 0, 0

        for r, ch in enumerate(word):
            if ch not in vowels:
                res = {v:0 for v in vowels}
                left = right = r + 1
                continue
            res[ch] += 1

            while all(res[v] > 0 for v in vowels):
                res[word[right]] -= 1
                right += 1
            number += right - left

        return number



