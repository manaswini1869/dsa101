class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # n = len(nums)
        # res = float('-inf')
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] < nums[j] and nums[j] - nums[i] > res:
        #             res = nums[j] - nums[i]
        # return res if res != float('-inf') else -1
        n = len(nums)
        ans, premin = -1, nums[0]
        for i in range(1, n):
            if nums[i] > premin:
                ans = max(ans, nums[i] - premin)
            else:
                premin = nums[i]
        return ans

