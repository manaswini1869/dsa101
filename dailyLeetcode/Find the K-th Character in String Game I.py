class Solution:
    def kthCharacter(self, k: int) -> str:
        count = k
        word = 'a'

        while len(word) < k:
            new_word = word
            count -= 1
            for i in word:
                req = ord(i) + 1
                new_word += chr(req)
            word = new_word
        return word[k-1]
