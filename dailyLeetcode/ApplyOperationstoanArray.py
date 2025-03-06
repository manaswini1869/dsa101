class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        num_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[num_non_zero], nums[i] = nums[i], nums[num_non_zero]
                num_non_zero += 1
        return nums