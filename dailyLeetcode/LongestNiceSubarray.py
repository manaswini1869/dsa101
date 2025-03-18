class Solution:
    # def niceCheck(self, niceArray: List[int]) -> bool:
    #     for i in range(len(niceArray)):
    #         for j in range(i+1, len(niceArray)):
    #             if (niceArray[i] & niceArray[j]):
    #                 return False
    #     return True
    # def longestNiceSubarray(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return 1
    #     left, right = 0, 1
    #     res = 0
    #     while right < len(nums):
    #         if self.niceCheck(nums[left:right+1]):
    #             res = max(res, right - left + 1)
    #             right += 1
    #         else:
    #             left += 1
    #     return res/
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, used, res = 0, 0, 0
        for right in range(len(nums)):
            while (used & nums[right] != 0):
                used ^= nums[left]
                left += 1
            used |= nums[right]
            res = max(res, right - left + 1)
        return res