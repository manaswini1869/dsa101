class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        a, b = 0, 2
        i, j = 1, 3
        if (s1 == s2) or (((s1[a] == s2[b] and s1[b] == s2[a]) or (s1[a] == s2[a] and s1[b] == s2[b])) and ((s1[i] == s2[j] and s1[j] == s2[i]) or (s1[i] == s2[i] and s1[j] == s2[j]))) :
            return True
        else:
            return False

