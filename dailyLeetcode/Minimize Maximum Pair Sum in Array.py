class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()

        n = len(nums)
        left, right = 0, n-1
        max_sum = float("-inf")

        while left < right:
            pair = nums[left] + nums[right]
            max_sum = max(max_sum, pair)

            left += 1
            right -= 1
        return max_sum






