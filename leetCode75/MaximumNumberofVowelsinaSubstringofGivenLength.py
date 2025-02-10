class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sunStr = s[:k]
        vowels = ['a', 'e', 'i', 'o', 'u']
        maxCount = 0
        currentCount = sum(1 for ch in sunStr if ch in vowels)
        maxCount = currentCount
        for i in range(k, len(s)):
            if s[i] in vowels:
                currentCount += 1
            if s[i-k] in vowels:
                currentCount -= 1
            maxCount = max(maxCount, currentCount)
        return maxCount
