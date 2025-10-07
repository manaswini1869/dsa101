class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n = len(gas)
        # tank = 0
        # index = -1
        # travel = 0

        # possible_index = []
        # for i in range(n):
        #     if gas[i] >= cost[i]:
        #         possible_index.append(i)


        # for i in possible_index:
        #     tank += gas[i]
        #     j = i
        #     while


        # return index
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        total = 0
        start = 0

        for i in range(n):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1

        return start












