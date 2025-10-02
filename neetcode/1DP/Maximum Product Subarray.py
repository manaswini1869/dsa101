class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # n = len(nums)
        # res = nums[0]

        # for i in range(n):
        #     curr = 1
        #     for j in range(i, n):
        #         curr *= nums[j]
        #         res = max(res, curr)

        # return res
        res = nums[0]
        curr_min, curr_max = 1, 1
        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1

            tmp = curr_max * n
            curr_max = max(curr_min*n, curr_max*n, n)
            curr_min = min(curr_min*n, n, tmp)
            res = max(res, curr_max)
        return res



