class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0

        nums.sort()
        min_score = float("inf")

        for i in range(len(nums)-k+1):
            min_score = min(min_score, nums[i+k-1] - nums[i])

        return min_score






