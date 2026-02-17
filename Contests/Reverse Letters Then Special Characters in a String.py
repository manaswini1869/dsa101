

class Solution:
    def reverseByType(self, s: str) -> str:

        s = list(s)
        n = len(s)

        left, right = 0, n-1
        while left < right:
            if not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        left, right = 0, n-1
        while left < right:
            if s[left].isalpha():
                left += 1
            elif s[right].isalpha():
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
        # time complexity = O(n)
        # space complexity = O(n)


        # n = len(s)
        # letters = []
        # chars = []
        # ans = []

        # for i in range(n):
        #     if s[i].isalpha():
        #         letters.append(s[i])
        #     else:
        #         chars.append(s[i])
        # i = 0
        # while letters or chars:
        #     if s[i].isalpha():
        #         ans.append(letters.pop())
        #     else:
        #         ans.append(chars.pop())
        #     i += 1
        # return ''.join(ans)

        # # time complexity : O(n)
        # # space complexity : O(n)


        

        




        