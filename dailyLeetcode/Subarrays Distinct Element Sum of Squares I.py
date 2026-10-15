class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        ans = 0

        n = len(nums)

        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr = len(set(nums[i:j+1]))
                ans += (curr*curr)
        return ans



        