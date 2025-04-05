class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        minHeap = []
        for interval in intervals:
            if minHeap and minHeap[0] <= interval[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval[1])

        return len(minHeap)