class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        empty = numBottles

        while empty >= numExchange:
            full_bottles += 1
            empty -= numExchange - 1
            numExchange += 1

        return full_bottles



