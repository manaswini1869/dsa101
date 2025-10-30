class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        n = len(nums)

        for r in range(n):
            if nums[r] != 0:
                nums[r], nums[non_zero] = nums[non_zero], nums[r]
                non_zero += 1

