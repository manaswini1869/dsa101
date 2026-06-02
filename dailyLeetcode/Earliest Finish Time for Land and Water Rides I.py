from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        n = len(landStartTime)
        m = len(waterStartTime)

        res = float("inf")
        for i in range(n):
            curr = landStartTime[i] + landDuration[i]
            for j in range(m):
                temp = max(curr, waterStartTime[j]) + waterDuration[j]

                res = min(res, temp)

                temp1 = waterStartTime[j] + waterDuration[j]
                temp = max(temp1, landStartTime[i]) + landDuration[i]

                res = min(res, temp)

        return res
    