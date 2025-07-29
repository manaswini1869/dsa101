class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [1] * n
        last = [0] * 32

        for i in range(n-1, -1, -1):
            for b in range(32):
                if (nums[i] & (1 << b)):
                    last[b] = i

            furthest = i
            for pos in last:
                furthest = max(furthest, pos)
            result[i] = furthest - i + 1
        return result
