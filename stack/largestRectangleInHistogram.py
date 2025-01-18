class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        height_stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while height_stack and height_stack[-1][1] > h:
                index, height = height_stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            height_stack.append(((start, h)))
        for i, h in height_stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area