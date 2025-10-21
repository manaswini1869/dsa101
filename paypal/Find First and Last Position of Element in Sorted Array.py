class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        res = [start, end]

        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                start = i
                end = i
                while end + 1 < n and nums[end+1] == target:
                    end += 1
                return [start, end]
        return res
