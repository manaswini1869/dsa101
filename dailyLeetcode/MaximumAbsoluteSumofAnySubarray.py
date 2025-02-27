class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = 0
        current_max = current_min = 0
        for num in nums:
            current_max = max(num, current_max + num)
            current_min = min(num, current_min + num)

            max_sum = max(max_sum, current_max)
            min_sum = min(min_sum, current_min)

        return max(abs(max_sum), abs(min_sum))
