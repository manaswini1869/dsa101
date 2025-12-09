class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_dict = {}

        for i, v in enumerate(nums):
            if v in hash_dict:
                return [hash_dict[v], i]
            hash_dict[target-v] = i
