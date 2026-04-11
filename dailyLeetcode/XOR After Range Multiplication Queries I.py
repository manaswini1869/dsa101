from typing import List
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        for query in queries:
            l, r, k, v = query
            idx = l

            while idx <= r:
                nums[idx] = (nums[idx]*v) % (10**9+7)
                idx += k
            
        ans = nums[0]
        for i in range(1, n):
            ans ^= nums[i]
        
        return ans


        