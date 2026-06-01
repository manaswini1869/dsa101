from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        n = len(cost)
        res = 0

        if n < 3:
            return sum(cost)

        cost.sort(reverse=True)
        i = 0
        while i < n:
            curr = cost[i:i+3]
            if len(curr) == 3:
                res += curr[0]+curr[1]
            else:
                res += sum(curr)
            i += 3
        return res