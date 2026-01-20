class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [-1]*n

        for i in range(n):
            curr = 0
            while curr < nums[i]:
                if curr | curr + 1 == nums[i]:
                    ans[i] = curr
                    break
                else:
                    curr += 1
        return ans


