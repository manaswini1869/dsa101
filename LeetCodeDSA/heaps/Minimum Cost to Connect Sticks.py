class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0

        heap = []
        for stick in sticks:
            heapq.heappush(heap, stick)

        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            cost += (x+y)
            heapq.heappush(heap, x+y)


        return cost












