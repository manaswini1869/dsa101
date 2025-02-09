class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         for k in range(j, len(nums)):
        #             if (i < j < k) and (nums[i]<nums[j]<nums[k]):
        #                 return True
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False
