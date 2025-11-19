class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        rep = set(["0", "10", "11"])
        n = len(bits)
        res = False
        i = 0
        while i < n:
            if str(bits[i]) in rep:
                i += 1
                res = True
            elif i + 1 < n and str(bits[i]) + str(bits[i+1]) in rep:
                i += 2
                res = False
        return res

