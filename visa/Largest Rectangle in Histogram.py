class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] -1
                max_area = max(max_area, height*width)

            stack.append(i)

        return max_area


        # left, right = 0, n-1

        # ans = float("-inf")

        # while left <= right:
        #     w = left - right + 1
        #     h = min(heights[left], heights[right])

        #     ans = max(ans, w*h)
        #     if heights[left] < heights[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return ans
        # ans = float("-inf")
        # for i in range(n):
        #     min_h = float('inf')
        #     for j in range(i, n):
        #         min_h = min(min_h, heights[j])
        #         ans = max(ans, min_h * (j - i + 1))
        # return ans






