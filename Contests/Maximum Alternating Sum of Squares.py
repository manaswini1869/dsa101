class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        nums = [-1*num if num < 0 else num for num in nums]
        nums.sort()

        n = len(nums)
        score = 0

        l, r = 0, n-1
        for i in range(n):
            if i % 2 == 0:
                score += (nums[r] * nums[r])
                r -= 1
            else:
                score -= (nums[l]* nums[l])
                l += 1

        return score