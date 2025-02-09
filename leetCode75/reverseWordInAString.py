class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()
        print(sList)
        i, j = 0, len(sList)-1
        while i < j:
            sList[i], sList[j] = sList[j], sList[i]
            i += 1
            j -= 1
        return " ".join(sList)
