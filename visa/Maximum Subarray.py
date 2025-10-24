class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        n = len(nums)

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum+nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum