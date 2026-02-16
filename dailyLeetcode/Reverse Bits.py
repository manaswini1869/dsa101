class Solution:
    def reverseBits(self, n: int) -> int:

        bin_n = bin(n)

        new_bin_n = str(bin_n)[2:][::-1]
        new_bin_n += '0'*(32 - len(new_bin_n))
        return int(new_bin_n, 2)

        # time complexity: O(1)
        # space complexity: O(1)



        