class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        left =  1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[left] = nums[i]
                left += 1
        return left
