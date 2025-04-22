from collections import defaultdict
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # linesweep ?
        points = defaultdict(int)
        for s, e, c in segments:
            points[s] += c
            points[e] -= c

        ans = []
        s = curTotal = 0
        for i in range(10**5+5):
            if i in points:
                if curTotal:
                    ans.append((s, i, curTotal))
                curTotal += points[i]
                s = i
        return ans