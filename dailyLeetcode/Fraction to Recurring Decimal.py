class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        if (numerator > 0) ^ (denominator > 0):
            res.append("-")

        a = abs(numerator)
        b = abs(denominator)

        res.append(str(a // b))
        reminder = a % b
        if reminder == 0:
            return "".join(res)
        res.append(".")
        d = {}

        while reminder:
            d[reminder] = len(res)
            reminder *= 10
            res.append(str(reminder // b))
            reminder = reminder%b
            if reminder in d:
                res.insert(d[reminder], "(")
                res.append(")")
                break



        return "".join(res)

