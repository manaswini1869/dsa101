class Solution:
    def processStr(self, s: str, k: int) -> str:
        lens = []
        res = 0
        for ch in s:
            if ch.islower():
                res += 1
            if ch == "*":
                if res:
                    res -= 1
            if ch == "#":
                res *= 2
            if ch == "%":
                pass
            lens.append(res)
        if k >= res:
            return "."
        
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            cur = lens[i]
            prev = lens[i - 1] if i > 0 else 0

            if ch.islower():
                if k == prev:
                    return ch

            elif ch == "#":
                k %= prev

            elif ch == "%":
                k = prev - 1 - k

            # '*' needs no index adjustment

        return "."
        


        