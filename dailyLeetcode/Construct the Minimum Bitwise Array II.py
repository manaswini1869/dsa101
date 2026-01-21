class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = []

        for i in range(n):

            if nums[i] == 2:
                ans.append(-1)
            else:
                for j in range(1, 32):
                    if ((nums[i] >> j) & 1) ^ 1:
                        ans.append(nums[i] ^ (1 << (j - 1)))
                        break

        return ans

        # for i in range(n):
        #     left, right = 1, nums[i]-1
        #     val = float("inf")
        #     while left <= right:
        #         mid = (left+right) // 2
        #         if mid | (mid+1) >= nums[i]:
        #             val = min(val, mid)
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     if val != float("inf"):
        #         ans[i] = val
        #     else:
        #         ans[i] = -1
        # return ans








