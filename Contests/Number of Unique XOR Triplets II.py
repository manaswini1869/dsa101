class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pairs, triplets = set(), set()
        for i,x in enumerate(nums):
            for j in nums[i:]:
                pairs.add(x^j)
        for pair in pairs:
            for z in nums:
                triplets.add(pair^z)
        return len(triplets)