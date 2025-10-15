class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # curr = nums[0]

        # n = len(nums)

        # i = 0
        # while i < n-1:
        #     if nums[i] == nums[i+1]:
        #         i += 2
        #     else:
        #         return nums[i]

        # return nums[i]

        res = 0

        for num in nums:
            res ^= num

        return res