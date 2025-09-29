class Solution:
    def climbStairs(self, n: int) -> int:

        # recursion
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2

        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # true 1DP Bottom up DP
        o, t = 1, 1

        for i in range(n-1):
            tmp = t
            t = o + t
            o = tmp

        return t

