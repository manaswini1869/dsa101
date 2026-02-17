from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        ans = []

        poss = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]

        def backtrack(idx, leds, hr, mi):
            if leds == turnedOn:
                if hr < 12 and mi < 60:
                    ans.append(f"{hr}:{mi:02d}")
                return 
            if idx == len(poss):
                return
            if idx < 4:
                backtrack(idx+1, leds+1, hr+poss[idx],mi)
            else:
                backtrack(idx+1, leds+1, hr,mi+poss[idx])
            backtrack(idx + 1, leds, hr, mi)
        backtrack(0, 0, 0, 0)
        return ans

        # time complexity = O(1)
        # space complexity = O(10) = O(1)

        # ans = []

        # for i in range(12):
        #     for j in range(60):
        #         if (bin(i).count('1')) + (bin(j).count('1')) == turnedOn:
        #             ans.append(f"{i}:{j:02d}")

        # return ans

        # # time complexity = O(12*60)
        # # space complexity = O(n) n = number of possiblities

        