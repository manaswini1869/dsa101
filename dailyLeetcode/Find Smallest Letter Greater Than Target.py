from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # n = len(letters)
        # for i in range(n):
        #     if letters[i] > target:
        #         return letters[i]
        # return letters[0]

        n = len(letters)
        left, right = 0, n-1
        ans_idx = -1
        while left <= right:
            mid = (left + right)//2
            if letters[mid] > target:
                ans_idx = mid
                right = mid - 1
            else:
                left = mid + 1
        if ans_idx == -1:
            return letters[0]
        return letters[ans_idx]        
        


        
        





