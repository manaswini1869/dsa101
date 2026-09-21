class Solution:
    def countCommas(self, n: int) -> int:

        count = 0
        divisor = 1000
        if n < 1000:
            return 0
        
        while divisor <= n:
            count += (n - divisor + 1)
            divisor *= 1000
        
        return count


        