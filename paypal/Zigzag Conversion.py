class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <=1:
            return s
        n = len(s)

        numCols = n

        res = [[""]* numCols for _ in range(numRows)]
        r, c = 0, 0
        i = 0
        while i < n: # to keep track of the string char
            while r < numRows and i < n:
                res[r][c] = s[i]
                r += 1
                i += 1
            r -= 2
            c += 1
            while r > 0 and i < n:
                res[r][c] = s[i]
                r -= 1
                c += 1
                i += 1
        return "".join("".join(row) for row in res )