class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        stack = []
        res = []
        for x, y in points:
            dist = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(stack, (dist, [x, y]))

        while k:
            k -= 1
            _, m = heapq.heappop(stack)
            res.append(m)

        return res

