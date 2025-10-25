class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        smallest_str = s

        for i in range(n):
            tmp1 = "".join(reversed(s[:i])) + s[i:]
            tmp2 = s[:i] + "".join(reversed(s[i:]))

            smallest_str = min(smallest_str, tmp1, tmp2)

        return smallest_str