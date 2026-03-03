class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        if k == 1:
            return "0"
        s1 = "0"
        while len(s1) <= k:
            stemp = "".join("1" if i == "0" else "0" for i in s1 )
            s1 = s1 + "1" + stemp[::-1]

        return s1[k-1]
        # time complexity : O(k)
        # space complexity : O(k)


        