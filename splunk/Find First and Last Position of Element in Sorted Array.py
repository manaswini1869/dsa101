class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        left, right = 0, n-1
        t = [-1, -1]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left >= n or nums[left] != target:
            return t
        t[0] = left
        while left < n and nums[left] == target:
            left += 1
        t[1] = left-1
        return t



