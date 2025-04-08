# class MedianFinder:

#     def __init__(self):
#         self.medium_ints = []
#         self.length = 0

#     def addNum(self, num: int) -> None:
#         self.length += 1
#         self.medium_ints.append(num)

#     def findMedian(self) -> float:
#         if self.length > 0:
#             self.medium_ints.sort()
#             if self.length % 2 == 0:
#                 n = self.length // 2
#                 return (self.medium_ints[n] + self.medium_ints[n-1]) / 2
#             else:
#                 return (self.medium_ints[self.length // 2])


class MedianFinder:

    def __init__(self):
        self.small, self.big = [], []

    def addNum(self, num: int) -> None:
        if self.big and self.big[0] < num:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -1*num)

        if len(self.small) > len(self.big) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        if len(self.big) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.big)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -1 * self.small[0]
        elif len(self.big) > len(self.small):
            return self.big[0]
        return (-1 * self.small[0] + self.big[0]) / 2

