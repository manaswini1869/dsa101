class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        def is_increaing(l, r):
            for i in range(l, r-1):
                if nums[i] >= nums[i+1]:
                    return False
            return True

        for i in range(n - (k+k)+1):
            if is_increaing(i, i+k) and is_increaing(i+k, i+k+k):
                return True
        return False


