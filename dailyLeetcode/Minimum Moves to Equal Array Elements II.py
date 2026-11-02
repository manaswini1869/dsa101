class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        n = len(nums)
        if len(set(nums)) == 1:
            return 0

        nums.sort()
        target = nums[n//2]

        # target = float('inf')
        # minSum = float('inf')
        # for i in range(n):
        #     curr = 0
        #     for j in range(n):
        #         curr += abs(nums[i] - nums[j])
        #     if curr < minSum:
        #         minSum = curr
        #         target = nums[i]
    
        return sum(abs(target - num) for num in nums)
        