class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        binary = str(bin(n))
        n = len(binary)
        for i in range(n-1, 1, -1):
            print(binary[i], i)
            if binary[i] == binary[i-1]:
                return False
        return True
        # time complexity : O(logn) n = len of the binary string
        # space complexity : O(logn) n = len of binary string 


        