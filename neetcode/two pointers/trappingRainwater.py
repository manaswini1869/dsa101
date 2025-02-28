# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if len(height) == 0:
#             return 0
#         prefix = [0] * len(height)
#         suffix = [0] * len(height)

#         prefix[0] = height[0]
#         for i in range(1, len(height)):
#             prefix[i] = max(prefix[i-1], height[i])

#         suffix[len(height)-1] = height[len(height)-1]
#         for i in range(len(height)-2, -1, -1):
#             suffix[i] = max(suffix[i+1], height[i])

#         print(suffix, prefix)
#         res = 0
#         for i in range(len(height)):
#             res += min(prefix[i], suffix[i]) - height[i]
#         return res

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
