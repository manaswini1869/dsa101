class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        answer = [0] * n
        answer[0] = cost[0]
        for i in range(1, len(cost)):
            answer[i] = min(answer[i-1], cost[i])
        return answer
