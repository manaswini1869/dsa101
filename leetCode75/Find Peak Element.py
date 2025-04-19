class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # # left, right = 0, n-1
        # for i in range(n-1):
        #     if nums[i] > nums[i+1]:
        #         return i
        # return n-1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l