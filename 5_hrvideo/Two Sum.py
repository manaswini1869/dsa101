class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return (i, j)

        n = len(nums)
        need_map = {}

        for k, v in enumerate(nums):
            need = target - v
            if need in need_map:
                return (k, need_map[need])
            else:
                need_map[v] = k