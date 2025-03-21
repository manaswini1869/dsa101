class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}
        for i in range(len(nums)):
            if (target - nums[i]) in target_map:
                return [i, target_map[target-nums[i]]]
            target_map[nums[i]] = i
