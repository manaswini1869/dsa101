# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         for l in range(len(nums)):
#             r = l + k
#             temp = nums[l:r]
#             if len(temp) == k:
#                 res.append(max(nums[l:r]))
#         print(res)
#         return res
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res