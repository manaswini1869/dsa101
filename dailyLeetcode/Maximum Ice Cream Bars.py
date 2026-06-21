from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        n = len(costs)
        # costs.sort()
        #  counting sort

        k = max(costs)
        freq = [0]*(k+1)
        output = [0]*len(costs)
        for cost in costs:
            freq[cost] += 1
        for i in range(1, len(freq)):
            freq[i] += freq[i-1]
        for cost in reversed(costs):
            output[freq[cost]-1] = cost
            freq[cost] -= 1
        count = 0
        if output[0] > coins:
            return 0
        for cost in output:
            if cost > coins:
                continue
            count += 1
            coins -= cost

        return count

        