class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        n2 = len(words)
        n1 = len(pattern)
        pattern = list(pattern)

        print()

        if n1 != n2:
            return False

        w_s = {}
        s_w = {}

        for i, j in zip(pattern, words):
            if i in w_s:
                if w_s[i] != j:
                    return False
            else:
                w_s[i] = j

            if j in s_w:
                if s_w[j] != i:
                    return False
            else:
                s_w[j] = i

        return True


