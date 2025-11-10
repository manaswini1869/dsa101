class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0

        n = len(nums)

        stack = [0]

        for num in nums:

            while stack and num < stack[-1]:
                stack.pop()
            if not stack or num > stack[-1]:
                ops += 1
                stack.append(num)

        return ops

