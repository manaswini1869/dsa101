class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # if len(sticks) < 2:
        #     return 0
        # sticks.sort(reverse=True)
        # costs = []
        # i = 1
        # while len(sticks) > 1:
        #     cost = sticks.pop() + sticks.pop()
        #     costs.append(cost)
        #     sticks.append(cost)
        #     sticks.sort(reverse=True)
        #     i += 1
        # return sum(x for x in costs)
        if len(sticks) < 2:
            return 0
        heapq.heapify(sticks)
        total_cost = 0
        while len(sticks) > 1:
            first, second = heapq.heappop(sticks), heapq.heappop(sticks)
            total_cost += first + second
            heapq.heappush(sticks, first+second)
        return total_cost