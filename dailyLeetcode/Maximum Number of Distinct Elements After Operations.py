class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        last = float("-inf")
        distinct = 0
        for num in nums:
            pos = max(last+1, num-k)
            if pos <= num+k:
                distinct += 1
                last = pos

        return distinct

