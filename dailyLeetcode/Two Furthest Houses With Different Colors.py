from typing import List
class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        n = len(colors)
        ans = float("-inf")

        d1 = 0
        for i in range(n-1, -1, -1):
            if colors[i] != colors[0]:
                d1 = i
                break
        d2 = 0
        for i in range(n):
            if colors[i] != colors[-1]:
                d2 = n - 1 - i
                break
        return max(d1, d2)



        # for i in range(n):
        #     for j in range(i+1, n):
        #         if colors[i] != colors[j]:
        #             ans = max(ans, j - i)
        # # i, j = 0, n-1
        
        # # while i <= j:
        # #     if colors[i] != colors[j]:
        # #         ans = max(ans, j - i)
        # #         i += 1
                
        # #     else:
        # #         j -= 1
        # return ans

        