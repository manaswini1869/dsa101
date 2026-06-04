class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        res = 0

        for i in range(num1, num2+1):
            s = str(i)
            if len(s) < 3:
                continue
            waviness = 0
            for j in range(1, len(s)-1):
                if s[j-1] < s[j] > s[j+1]:
                    waviness += 1
                if s[j-1] > s[j] < s[j+1]:
                    waviness += 1
            res += waviness


        return res


        