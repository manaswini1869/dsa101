class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = len(height)
        max_water = float("-inf")
        left, right = 0, n-1

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h*w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


