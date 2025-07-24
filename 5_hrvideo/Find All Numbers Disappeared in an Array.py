class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # res = []
        # n = len(nums)
        # seen = set(nums)
        # for i in range(1, n+1):
        #     if i not in seen:
        #         res.append(i)
        # return res
        n = len(nums)
        res = []
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1

        for i in range(1, n+1):
            if nums[i-1] > 0:
                res.append(i)

        return res

