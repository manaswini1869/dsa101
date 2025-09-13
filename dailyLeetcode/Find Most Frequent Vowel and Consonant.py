class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        vowels_map = {}
        consonants_map = {}
        for i in s:
            if i in vowels:
                vowels_map[i] = vowels_map.get(i, 0) + 1
            else:
                consonants_map[i] = consonants_map.get(i, 0) + 1

        return max(vowels_map.values(), default=0) + max(consonants_map.values(), default=0)
