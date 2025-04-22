class Solution:
    def similarPairs(self, words: List[str]) -> int:
        pairs = 0
        n = len(words)
        for i in range(n):
            word1 = set(words[i])
            for j in range(i+1, n):
                word2 = set(words[j])
                if word1 == word2:
                    pairs += 1
        return pairs