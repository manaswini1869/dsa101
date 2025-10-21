class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        res = float("-inf")
        while left < right:
            res = max(res, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res