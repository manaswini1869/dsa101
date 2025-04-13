class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum_nums = sum(nums)
        reminder = sum_nums % k
        if sum_nums > k or sum_nums < k :
            return reminder
        else:
            return 0