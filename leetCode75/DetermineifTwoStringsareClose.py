class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if (len(word1) != len(word2)) or  (set(word1) != set(word2)):
            return False
        h1, h2 = {}, {}
        for i in word1:
            h1[i] = h1.get(i, 0) + 1
        for i in word2:
            h2[i] = h2.get(i, 0) + 1
        val1 = sorted(h1.values())
        val2 = sorted(h2.values())

        return val1 == val2