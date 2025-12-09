class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # res = []
        # n = len(nums)
        # nums = set(nums)
        # for i in range(1, n+1):
        #     if i not in nums:
        #         res.append(i)

        # return res

        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res


