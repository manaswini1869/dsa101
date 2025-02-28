class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        for l in range(len(s2)):
            temp = s2[l:r]
            r += 1
            if(sorted(temp) == sorted(s1)):
                return True
        return False