class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        i = 0
        while i < n:
            part = s[i:i+k]
            if len(part) != k:
                part += fill * (k - len(part))
            res.append(part)
            i += k

        return res
