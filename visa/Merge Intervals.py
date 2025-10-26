class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        res = [intervals[0]]

        n = len(intervals)

        for i in range(1, n):
            curr_s, curr_e = intervals[i]
            if curr_s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], curr_e)
            else:
                res.append(intervals[i])

        return res


