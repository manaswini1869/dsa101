class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        return prefix_sum
