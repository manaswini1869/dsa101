class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            sum1 = sum(nums[i:])
            sum2 = sum(nums[:i])
            print(sum1, sum2)
            if sum1 == sum2:
                return True
        return False
