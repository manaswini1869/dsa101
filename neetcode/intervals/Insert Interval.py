class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x[0])

        # i = 0
        # while intervals and i < len(intervals)-1:
        #     if intervals[i][1] >= intervals[i+1][0]:
        #         intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
        #         del intervals[i+1]
        #     else:
        #         i += 1


        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval=[
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1]),
                ]

        res.append(newInterval)

        return res

