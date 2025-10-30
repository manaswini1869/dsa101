class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)

        p = [nums[0]]

        for i in range(1, n):
            p.append(p[-1] + nums[i])

        total = p[-1]
        for i in range(n):
            left_sum = p[i - 1] if i > 0 else 0
            right_sum = total - p[i]
            if left_sum == right_sum:
                return i
        return -1

