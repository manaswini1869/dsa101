class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        ans = [intervals[0]]

        for x, y in intervals[1:]:
            if x <= ans[-1][1]:
                ans[-1][0], ans[-1][1] = min(ans[-1][0], x), max(ans[-1][1], y)
            else:
                ans.append([x, y])
        return ans





