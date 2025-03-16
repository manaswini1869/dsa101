from collections import Counter
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            vowels = defaultdict(int)
            non_vowel_count = 0
            res = 0
            l = 0
            for r in range(len(word)):
                if word[r] in "aeiou":
                    vowels[word[r]] += 1
                else:
                    non_vowel_count += 1
                while len(vowels) == 5 and non_vowel_count >= k:
                    res += (len(word) - r)
                    if word[l] in "aeiou":
                        vowels[word[l]] -= 1
                    else:
                        non_vowel_count -= 1
                    if vowels[word[l]] == 0:
                        vowels.pop(word[l])
                    l += 1
            return res
        return atleastk(k) - atleastk(k+1)