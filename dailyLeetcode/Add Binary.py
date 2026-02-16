class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a)-1
        j = len(b)-1

        carry = 0
        ans = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1
            ans.append(str(total % 2))
            carry = total // 2
        
        # time complexity = O(max(len(a), len(b)))
        # space complexity = O(max(len(a), len(b)))


        
        return ''.join(reversed(ans))


        # a = int(a, 2)
        # b = int(b, 2)
        # return bin(a+b)[2:]

        # # time complexity = O(max(len(a), len(b))
        # # space complexit = O(max(len(a), len(b))

        



        