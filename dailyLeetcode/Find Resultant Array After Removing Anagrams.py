class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        result = [words[0]]

        n = len(words)

        for i in range(1, n):
            if sorted(result[-1]) != sorted(words[i]):
                result.append(words[i])

        return result




