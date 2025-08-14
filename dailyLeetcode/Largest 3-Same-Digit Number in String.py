class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        n = len(num)
        for i in range(n-2):
            if num[i] == num[i+1] == num[i+2]:
                if res == "" or num[i] > res[0]:
                    res = num[i:i+3]
        return res