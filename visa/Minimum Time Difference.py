class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        n = len(timePoints)

        ans = float("inf")
        mins = []

        for i in range(n):
            m = int(timePoints[i][:2]) * 60 + int(timePoints[i][3:])
            mins.append(m)
        mins.sort()

        mins.append(mins[0] + 1440)
        n = len(mins)
        for i in range(1, n):
            ans = min(ans, mins[i] - mins[i-1])

        return ans