class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = {}

        for k, v in enumerate(nums):
            if (target - v) in res:
                return [k, res[target-v]]
            else:
                res[v] = k

        return []