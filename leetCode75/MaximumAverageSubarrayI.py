class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumk = sum(nums[:k])
        maxAvg = sumk
        for i in range(k, len(nums)):
            sumk += nums[i] - nums[i-k]
            maxAvg = max(maxAvg, sumk)
        return maxAvg/k