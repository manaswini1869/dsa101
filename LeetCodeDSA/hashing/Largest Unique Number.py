class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        b, c = set(), set()

        for num in nums:
            if num in c:
                b.add(num)
            else:
                c.add(num)

        a = c - b
        if not a:
            return -1

        return max(a)

#         prev_set = set([nums[0]])
#         prev = nums[0]

#         n = len(nums)

#         for i in range(1, n):
#             if nums[i] in prev_set:
#                 prev =
#             else:
#                 prev = max(prev, nums[i])
#                 prev_set.add(nums[i])

#             print(prev, prev_set)

#         return prev if prev != float("-inf") else -1



