class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSum = 0
        curSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curSum += nums[i]
            else:
                maxSum = max(maxSum, curSum)
                curSum = nums[i]
        maxSum = max(maxSum, curSum)
        return maxSum
