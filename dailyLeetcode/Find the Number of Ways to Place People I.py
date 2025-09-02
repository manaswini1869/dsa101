class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        points.sort(key=lambda p: (p[0], -p[1]))
        for i in range(n):
            max_y = float("-inf")
            for j in range(i+1, n):
                x2, y2 = points[j]
                x1, y1 = points[i]

                if y2 <= y1 and y2 > max_y:
                    res += 1
                    max_y = y2

        return res