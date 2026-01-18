class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:

        ans = []

        for x, y, c in towers:
            dist = abs(center[0] - x) + abs(center[1]-y)
            if dist <= radius:
                heapq.heappush(ans, (-c, x, y))
        if ans:
            _, x, y = heapq.heappop(ans)
            return [x, y]
        return [-1, -1]




