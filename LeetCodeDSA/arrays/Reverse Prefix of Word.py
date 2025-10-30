class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        word = list(word)
        n = len(word)
        idx = -1

        for i in range(n):
            if word[i] == ch:
                idx = i
                break

        if idx == -1:
            return "".join(word)

        subarr = word[:idx+1] #[::-1]
        l, r = 0, idx
        while l <= r:
            subarr[l], subarr[r] = subarr[r], subarr[l]
            l += 1
            r -= 1
        return "".join(subarr + word[idx+1:])

