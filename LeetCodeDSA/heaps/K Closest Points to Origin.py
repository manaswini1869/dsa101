class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []
        for x, y in points:
            dist = (x)**2 + (y)**2
            heapq.heappush(min_heap, (-dist, (x, y)))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [[point[0], point[1]] for _, point in min_heap]











