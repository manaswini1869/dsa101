class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()

        n = len(nums)

        left, right = 0, 1

        while right < n:
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                if left > 0:
                    left -= 1
                    right -= 1

            else:
                left += 1
                right += 1