class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        n = len(nums)
        for i in range(n):
            if (target - nums[i]) in freq:
                return [i, freq[target-nums[i]]]
            freq[nums[i]] = i