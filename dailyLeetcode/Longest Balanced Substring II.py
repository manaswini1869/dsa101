from collections import Counter
class Solution:
    def longestBalanced(self, s: str) -> int:

        def calc1(s: str) -> int:
            res = 0
            i, n = 0, len(s)
            while i < n:
                j = i + 1
                while j < n and s[j] == s[i]:
                    j += 1
                res = max(res, j - i)
                i = j
            return res

        def calc2(s: str, a: str, b: str) -> int:
            res = 0
            i, n = 0, len(s)
            while i < n:
                while i < n and s[i] not in (a, b):
                    i += 1
                pos = {0: i - 1}
                d = 0
                while i < n and s[i] in (a, b):
                    d += 1 if s[i] == a else -1
                    if d in pos:
                        res = max(res, i - pos[d])
                    else:
                        pos[d] = i
                    i += 1
            return res

        def calc3(s: str) -> int:
            pos = {(0, 0): -1}
            cnt = Counter()
            res = 0
            for i, c in enumerate(s):
                cnt[c] += 1
                k = (cnt["a"] - cnt["b"], cnt["b"] - cnt["c"])
                if k in pos:
                    res = max(res, i - pos[k])
                else:
                    pos[k] = i
            return res

        x = calc1(s)
        y = max(calc2(s, "a", "b"), calc2(s, "b", "c"), calc2(s, "a", "c"))
        z = calc3(s)
        return max(x, y, z)



        # n = len(s)
        # max_size = 1
        # counter = defaultdict(int)
        # for i in range(n):
        #     counter[s[i]] += 1
        #     for j in range(i+1, n):
        #         counter[s[j]] += 1
        #         if len(set(counter.values())) == 1:
        #             max_size = max(max_size, j-i+1)
        #     counter = defaultdict(int)
        # return max_size


        # # time complexity = O(n**2)
        # # space complexity = O(n)



        