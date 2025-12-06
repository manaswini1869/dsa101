class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        stack = []
        n = len(nums)

        for i in range(n):
            while stack and nums[i] < nums[stack[-1]] and len(stack)-1 +(n-i) >= k:
                stack.pop()
            stack.append(i)


        return [nums[i] for i in stack[:k]]


