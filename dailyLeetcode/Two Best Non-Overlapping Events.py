class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        events.sort(key=lambda x: x[0])

        max_sum = 0
        max_single = 0
        heap = []

        for st, et, val in events:
            while heap and heap[0][0] < st:
                _, best_val = heapq.heappop(heap)
                max_single = max(max_single, best_val)

            max_sum = max(max_sum, val + max_single)

            heapq.heappush(heap, (et, val))
            max_sum = max(max_sum, val)


        return max_sum

        # final = float("-inf")
        # events.sort(key=lambda x:-x[2])

        # n = len(events)

        # for i in range(n):

        #     st, et, val = events[i]

        #     final = max(final, val)

        #     for j in range(n):
        #         if i == j:
        #             continue
        #         st1, et1, val1 = events[j]
        #         if st1 >= et + 1 or st >= et1 + 1:
        #             curr_val = val + val1
        #             final = max(final, curr_val)

        # return final






        return final











