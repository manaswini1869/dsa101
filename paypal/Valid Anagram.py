class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)

        if n1 != n2:
            return False

        h1 = {}
        h2 = {}
        for i in range(n1):
            h1[s[i]] = h1.get(s[i], 0) + 1
            h2[t[i]] = h2.get(t[i], 0) + 1

        return h1 == h2