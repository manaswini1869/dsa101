class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if nums[0] == 1:
            last = 0
        else:
            last = -1

        for i in range(1, n):
            if nums[i] == 1 and last!=-1 and (i-last) <= k:
                return False
            if nums[i] == 1:
                last = i
        return True


