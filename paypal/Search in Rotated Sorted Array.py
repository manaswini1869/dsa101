class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)

        left, right = 0, n-1
        pivot = 0
        if nums[pivot] == target:
            return pivot
        while left < right: # left has the smallest number index
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        # left will be the pivot index with the lowest element in the nums
        # everything on the left of left is greated than nums[left]
        pivot = left
        left, right = 0, n-1

        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1





