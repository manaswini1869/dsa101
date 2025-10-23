class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2:
            if s[0] == s[1]:
                return True
            else:
                return False
        res = ""
        n = len(s)
        for i in range(1, n):
            tmp = (int(s[i-1]) + int(s[i])) % 10
            res += str(tmp)

        return self.hasSameDigits(res)