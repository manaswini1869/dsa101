class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        res = 0
        l, r = 0, n-1
        left, right = height[l], height[r]
        while l < r:
            if left < right:
                l += 1
                left = max(left, height[l])
                res += left - height[l]

            else:
                r -= 1
                right = max(right, height[r])
                res += right - height[r]
        return res
