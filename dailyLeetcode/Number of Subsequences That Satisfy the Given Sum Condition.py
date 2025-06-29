class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        count = 0
        nums = sorted(nums)
        MOD = 10**9+7
        n = len(nums)
        left, right = 0, n - 1
        while left <= right :
            min_val = nums[left]
            max_val = nums[right]
            if min_val + max_val <= target:
                count = (count + pow(2, right - left, MOD)) % MOD
                left += 1
            else:
                right -= 1


        return count