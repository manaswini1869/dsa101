class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = [0]*(n+1)
        # for i in range(n+1):
        #     x = bin(i)[2:]
        #     count = 0
        #     for j in x:
        #         if j == '1':
        #             count += 1
        #     ans[i] = count
        # return ans
        def popcount(x):
            count = 0
            while x!=0:
                x &= x - 1
                count += 1
            return count

        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i] = popcount(i)
        return ans
