class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        mapper1 = Counter(s1)
        mapper2 = Counter(s2[:n1])

        if mapper1 == mapper2:
            return True

        for i in range(n1, n2):
            mapper2[s2[i]] += 1
            mapper2[s2[i - n1]] -= 1
            if mapper2[s2[i - n1]] == 0:
                del mapper2[s2[i - n1]]
            if mapper1 == mapper2:
                return True

        return False


        # n = len(s2)
        # mapper = Counter(s1)

        # for i in range(n):
        #     mapper2 = mapper.copy()
        #     if s2[i] in mapper2:
        #         j = i
        #         print(mapper2)
        #         while j < n and s2[j] in mapper2 and mapper2[s2[j]] > 0:
        #             mapper2[s2[j]] -= 1
        #             j += 1
        #         if (j - i) == len(s1):
        #             return True
        # return False

