class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        x1, y1 = points.pop(0)

        while points:
            x2, y2 = points.pop(0)
            time += max(abs(y1-y2), abs(x1-x2))
            x1, y1 = x2, y2

        return time

