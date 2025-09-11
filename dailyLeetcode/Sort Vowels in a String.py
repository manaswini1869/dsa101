class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        vowels = set("AEIOUaeiou")
        t = []
        vowel = []
        for i in range(n):
            if s[i] in vowels:
                t.append("*")
                vowel.append(s[i])
            else:
                t.append(s[i])
        vowel.sort(reverse=True)
        for i in range(n):
            if t[i] == "*":
                t[i] = vowel.pop()
        return "".join(t)
