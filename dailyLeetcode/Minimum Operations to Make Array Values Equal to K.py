class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique = set()
        for i in nums:
            if i < k:
                return -1
            elif i > k:
                unique.add(i)
        return len(unique)