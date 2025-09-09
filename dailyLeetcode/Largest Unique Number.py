class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        res = -1
        for key, val in freq.items():
            if val == 1:
                res = max(key, res)
        return res
