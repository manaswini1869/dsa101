class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        sList = list(s)
        vowelsInS = []
        for i in s:
            if i in vowels:
                vowelsInS.append(i)
        for i in range(len(s)):
            if s[i] in vowels:
                sList[i] = vowelsInS.pop()
        return "".join(sList)