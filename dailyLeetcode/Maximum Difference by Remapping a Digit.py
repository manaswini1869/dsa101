class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_num = float('-inf')
        min_num = float('inf')
        nums = str(num)
        for i in nums:
            max_num_tmp = int(nums.replace(i, '9'))
            min_num_tmp = int(nums.replace(i, '0'))
            max_num = max(max_num, max_num_tmp)
            min_num = min(min_num_tmp, min_num)
        return max_num - min_num