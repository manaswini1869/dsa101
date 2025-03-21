import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance_map = []

        # for point in points:
        #     print(point)
        #     distance = math.pow((math.pow((point[0] - 0), 2) + math.pow((point[1] - 0), 2)), 0.5)
        #     distance_map.append((distance, point))
        # sorted_map = sorted(distance_map)
        # closest_points = [point for _, point in sorted_map[:k]]
        # return closest_points
        minHeap = []
        for x,y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res

