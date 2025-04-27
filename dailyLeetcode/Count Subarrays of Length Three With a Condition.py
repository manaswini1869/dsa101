class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        count = 0
        while left + 2 < n:
            if nums[left] + nums[left+2] == nums[left+1] / 2:
                count += 1
            left += 1
        return count