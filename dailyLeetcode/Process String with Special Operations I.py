class Solution:
    def processStr(self, s: str) -> str:

        res = ""
        for ch in s:
            if ch.islower():
                res += ch
            if ch == "*":
                if res:
                    res = res[:-1]
            if ch == "#":
                res += res
            if ch == "%":
                res = res[::-1]

        return res


        