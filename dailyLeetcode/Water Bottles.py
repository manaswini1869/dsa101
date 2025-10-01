class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        empties = 0
        while numBottles > 0:
            res += numBottles
            empties += numBottles
            numBottles = 0

            numBottles = empties // numExchange
            empties = empties % numExchange

        return res

