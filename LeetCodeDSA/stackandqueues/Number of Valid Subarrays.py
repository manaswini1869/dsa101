# class Solution:
#     def validSubarrays(self, nums: List[int]) -> int:

#         n = len(nums)
#         if n == 1:
#             return 1
#         stack = []
#         count = 0

#         for i in range(n):
#             stack.append(nums[i])
#             count += 1
#             j = i+1
#             while j < n and stack[0] <= nums[j]:
#                 count += 1
#                 j += 1
#             while stack:
#                 stack.pop()
#         return count

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return 1
        stack = []
        count = 0

        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                count += (i - stack[-1])
                stack.pop()
            stack.append(i)
        while stack:
            count += n - stack[-1]
            stack.pop()
        return count




