class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # word = 'a'
        # for i in operations:
        #     count = k
        #     print(word)
        #     if i == 0:
        #         word += word
        #     else:
        #         while count > 0:
        #             new_word = ""
        #             count -= 1
        #             for j in word:
        #                 req = ord(j) + 1
        #                 new_word += chr(req)
        #         word += new_word
        # return word[k-1]
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1
        return chr(ord("a") + (ans % 26))
