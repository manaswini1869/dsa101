class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ranMap, magMap = {}, {}
        for i in ransomNote:
            ranMap[i] = ranMap.get(i, 0) + 1
        for i in magazine:
            magMap[i] = magMap.get(i,0) + 1
        for char, count in ranMap.items():
            if magMap.get(char, 0) < count:
                return False
        return True