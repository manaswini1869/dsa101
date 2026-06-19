class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        highest = 0
        res = 0
        for g in gain:

            highest += g
            res = max(res, highest)


        return res     

        