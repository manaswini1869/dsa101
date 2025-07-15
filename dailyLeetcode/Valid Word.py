class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if len(word) < 3:
            return False
        vowel_check = False
        conso_check = False
        if word.isalnum():
            for i in word:
                if i in vowels:
                    vowel_check = True
                if i.isalpha() and i not in vowels:
                    conso_check = True
        else:
            return False
        return True if vowel_check and conso_check else False
