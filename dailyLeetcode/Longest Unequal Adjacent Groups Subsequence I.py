class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        if n == 0:
            return []

        result = [words[0]]
        prev_group = groups[0]

        for i in range(1, n):
            if groups[i] != prev_group:
                result.append(words[i])
                prev_group = groups[i]
        return result