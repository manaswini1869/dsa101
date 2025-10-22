class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        if n <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, n):
            s, e = intervals[i]
            if res[-1][1] >= s:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])

        return res