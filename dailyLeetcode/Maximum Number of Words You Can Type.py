class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        count = 0
        text = text.split()

        for word in text:
            word = set(word)
            can_type = True
            for i in brokenLetters:
                if i in word:
                    can_type = False
            if can_type:
                count += 1
        return count