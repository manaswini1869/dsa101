class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count = 0
        mapper = defaultdict(int)
        mapper[0] = 1
        n = len(nums)
        prefix = 0

        for i in range(n):
            prefix += nums[i]
            count += mapper[prefix - goal]
            mapper[prefix] += 1

        return count



