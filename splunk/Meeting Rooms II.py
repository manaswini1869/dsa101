class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        heap = []
        intervals.sort()
        heapq.heappush(heap, intervals[0][1])
        for interval in intervals[1:]:
            if heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        return len(heap)




