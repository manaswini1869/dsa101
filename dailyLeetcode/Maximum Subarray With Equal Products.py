class Solution:
    def maxLength(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0

        bound = lcm(*nums) * max(nums)

        for i in range(n):
            prod = 1
            lc = 1
            gc = 0
            for j in range(i, n):
                prod *= nums[j]
                gc = gcd(gc, nums[j])
                lc = lcm(lc, nums[j])

                if prod == gc * lc:
                    ans = max(ans, len(nums[i:j+1]))
                if prod > bound:
                    break
        return ans
