class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        count = 0
        events = sorted(events, key=lambda x: x[0])
        queue = []
        day = 1
        i = 0
        n = len(events)
        last = max(end for _, end in events)
        while day <= last:

            while i < n and events[i][0] == day:
                heapq.heappush(queue, events[i][1])
                i += 1

            while queue and queue[0] < day:
                heapq.heappop(queue)

            if queue:
                heapq.heappop(queue)
                count += 1
            day += 1

        return count

