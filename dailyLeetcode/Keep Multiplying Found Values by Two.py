class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        n = len(nums)

        while original in set(nums):
            original *= 2

        return original

