class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for i in range(n):
            curr_min, curr_max = nums[i], nums[i]
            for j in range(i+1, n):
                curr_min, curr_max = min(curr_min, nums[j]), max(curr_max, nums[j])
                total += (curr_max - curr_min)

        return total