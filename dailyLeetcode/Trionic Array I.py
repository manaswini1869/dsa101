class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        n = len(nums)
        i = 1

        while i < n and nums[i] > nums[i-1]:
            i += 1
        if i == 1 or i == n:
            return False
        p = i-1

        while i < n and nums[i] < nums[i-1]:
            i += 1
        if i == p+1 or i == n:
            return False
        q = i-1
        while i < n and nums[i] > nums[i-1]:
            i += 1
        
        return i == n






        