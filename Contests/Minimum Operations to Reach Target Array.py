class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:

        n = len(nums)
        ops = set()
        for i in range(n):
            if nums[i] != target[i]:
                ops.add(nums[i])

        return len(ops)



