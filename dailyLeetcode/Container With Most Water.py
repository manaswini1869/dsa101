class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = float("-inf")

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            max_water = max(max_water, h*w)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_water
