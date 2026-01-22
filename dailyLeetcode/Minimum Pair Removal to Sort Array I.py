class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        n = len(nums)


        def check(nums):
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    return False
            return True
        ops = 0
        while not check(nums):
            min_sum = float("inf")
            min_idx = -1
            for i in range(1, len(nums)):
                if nums[i-1] + nums[i] < min_sum:
                    min_sum = nums[i-1] + nums[i]
                    min_idx = i-1

            nums.pop(min_idx+1)
            nums[min_idx] = min_sum
            ops += 1

        return ops


