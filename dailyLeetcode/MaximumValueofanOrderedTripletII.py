class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_i = [0] * n
        max_i[0] = nums[0]
        for i in range(1, n):
            max_i[i] = max(nums[i], max_i[i-1])

        max_k = [0] * n
        max_k[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            max_k[i] = max(max_k[i+1], nums[i])

        res = 0
        for i in range(1, n-1):
            res = max(res, ((max_i[i-1] - nums[i]) * max_k[i+1]))
        print(res)
        return res