from typing import List
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()

        arr[0] = 1
        n = len(arr)

        for i in range(1, n):
            d = max(0, arr[i] - arr[i-1] - 1)
            arr[i] -= d
        
        return max(arr)

            



        