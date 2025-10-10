"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)

        res, count = 0, 0
        start = sorted([i.start for i in intervals ])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -=1
            res = max(count, res)

        return res






