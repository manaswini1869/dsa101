class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        mapper1 = defaultdict(int)
        mapper2 = defaultdict(int)

        n1 = len(word1)
        n2 = len(word2)

        if n1 != n2:
            return False

        for i in range(n1):
            mapper1[word1[i]] += 1
            mapper2[word2[i]] += 1

        return mapper1.keys() == mapper2.keys() and sorted(mapper1.values()) == sorted(mapper2.values())

