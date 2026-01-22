class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(p)

        n = len(s)
        start, end = 0, n1
        if n < n1:
            return []
        if n == n1:
            if sorted(p) == sorted(s):
                return [0]
        res = []
        p = Counter(p)
        curr = Counter(s[start:end])
        while end <= n:
            if  curr == p:
                res.append(start)
            curr[s[start]] -= 1
            start += 1
            if end < n:
                curr[s[end]] += 1
            end += 1
        return res



