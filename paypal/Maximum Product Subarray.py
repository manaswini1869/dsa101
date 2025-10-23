class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = f = g = nums[0]
        for i in range(1, n):
            ff, gg = f, g
            f = max(nums[i], ff*nums[i], gg*nums[i])
            g = min(nums[i], gg*nums[i], ff*nums[i])
            ans = max(ans, f)

        return ans


