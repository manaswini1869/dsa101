class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        # nums = set(nums)
        # for i in range(n+1):
        #     if i not in nums:
        #         return i

        expected_sum = sum(i for i in range(n+1))
        return expected_sum - sum(nums)

