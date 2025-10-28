class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        no_arr = 0

        left = 0
        curr_prod = 1

        for right in range(n):
            curr_prod *= nums[right]
            while curr_prod >= k and left <= right:
                curr_prod /= nums[left]
                left += 1
            no_arr += right - left + 1
        return no_arr


