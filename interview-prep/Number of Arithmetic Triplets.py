class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        # count = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[j] - nums[i] == diff:
        #             for k in range(j+1, n):
        #                 if nums[k] - nums[j] == diff:
        #                     count += 1
        # return count
        count = 0
        nums_set = set(nums)
        for num in nums_set:
            if num + diff in nums_set and num+2*diff in nums_set:
                count += 1
        return count