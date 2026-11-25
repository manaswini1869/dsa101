class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        ones = min(cost1 * need1, costBoth*need1)

        twos = min(cost2 * need2, costBoth*need2)

        rem = min(need1, need2)

        bts = costBoth * rem

        bts += cost1 * (need1 - rem)
        bts += cost2 * (need2 - rem)

        both = costBoth * max(need1, need2)

        return min(ones + twos, bts, both)
