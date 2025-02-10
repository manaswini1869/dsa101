class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        i, j = 0, len(height) - 1
        while i < j:
            heightPres = min(height[i], height[j])
            widthPres = abs(j - i)
            maxWater = max(maxWater, heightPres * widthPres)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return maxWater
