from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        less = []
        more = []
        same = []
        for num in nums:
            if num > pivot:
                more.append(num)
            elif num < pivot:
                less.append(num)
            else:
                same.append(num)
        return less + same + more



        