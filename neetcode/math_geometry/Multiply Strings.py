class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if "0" in [num1, num2]:
            return "0"

        n1 = len(num1)
        n2 = len(num2)

        res = [0]*(n1+n2)

        num1, num2 = num1[::-1], num2[::-1]

        for i in range(n1):
            for j in range(n2):
                dig = int(num1[i]) * int(num2[j])
                res[i+j] += dig
                res[i+j+1] += res[i+j] // 10
                res[i+j] = res[i+j] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])

        return "".join(res)




