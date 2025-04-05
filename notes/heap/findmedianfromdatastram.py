class MedianFinder:

    def __init__(self):
        # self.median_finder = []
        # self.n = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # self.median_finder.append(num)
        # self.median_finder.sort()
        # self.n += 1
        if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap) :
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # if len(self.median_finder) % 2 == 0:
        #     return (self.median_finder[self.n // 2] + self.median_finder[(self.n // 2) - 1] ) / 2
        # else:
        #     return self.median_finder[self.n // 2]
        if (len(self.max_heap)) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()