class Solution:
    def counter(self, arr):
        arr_map = {}
        for i in arr:
            arr_map[i] = arr_map.get(i, 0) + 1
        return arr_map
    def check_all_ones(self, arr):
        return all(i==1 for i in arr)
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        nums_map = self.counter(nums)
        while self.check_all_ones(nums_map.values()) == False:
            operations += 1
            nums = nums[3:]
            nums_map = self.counter(nums)
        return operations