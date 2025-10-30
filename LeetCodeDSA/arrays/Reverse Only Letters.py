class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = list(s)
        n = len(res)
        left, right = 0, n-1

        while left <= right:
            if res[left].isalpha() and res[right].isalpha():
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1
            elif not res[left].isalpha():
                left += 1
            elif not res[right].isalpha():
                right -= 1
        return "".join(res)


