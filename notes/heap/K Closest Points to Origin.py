class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_point = []
        minHeap = []
        for point in points:
            distance = math.sqrt((pow(point[0], 2) + pow(point[1], 2)))
            distance_point.append((-1*distance, point))
        for distance in distance_point:
            heapq.heappush(minHeap, distance)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        print(minHeap)
        return [point[1] for point in minHeap ]