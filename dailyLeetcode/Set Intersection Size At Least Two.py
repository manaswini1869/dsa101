class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:

        intervals.sort(key= lambda x: (x[1],-x[0])) # sort the end in ASC and start in DESC
        p1 = -1
        p2 = -1

        res = 0

        for left, right in intervals:
            if left > p2:
                res += 2
                p1 = right - 1
                p2 = right
            elif left > p1:
                res += 1
                p1 = p2
                p2 = right



        return res


