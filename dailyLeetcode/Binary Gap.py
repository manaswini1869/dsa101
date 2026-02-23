class Solution:
    def binaryGap(self, n: int) -> int:
        
        bin_str = str(bin(n))[2:]

        n = len(bin_str)
        prev = -1
        ans = 0

        for i in range(n):
            if bin_str[i] == '1':
                if prev != -1:
                    ans = max(ans, i - prev)
                prev = i


        return ans





        