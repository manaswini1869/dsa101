class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # n = len(queries)
        # res = [-1]*n

        # for i in range(n):
        #     val = float("inf")
        #     for start, end in intervals:
        #         if start > queries[i]:
        #             break
        #         if start <= queries[i] <= end:
        #             val = min(val, end - start + 1)
        #     if val != float("inf"):
        #         res[i] = val

        # return res


        res = {} # query and the interval length
        min_heap = []
        i = 0
        intervals.sort()
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0]+1, intervals[i][1]))
                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)


            res[q] = min_heap[0][0] if min_heap else -1


        return [res[q] for q in queries]







