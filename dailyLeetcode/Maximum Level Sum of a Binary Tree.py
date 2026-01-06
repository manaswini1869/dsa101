# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        max_sum = float("-inf")
        ans = 1
        stack = deque([root])
        while stack:
            level_sum = 0
            n = len(stack)
            for _ in range(n):
                curr_node = stack.popleft()
                level_sum += curr_node.val
                if curr_node.left:
                    stack.append(curr_node.left)
                if curr_node.right:
                    stack.append(curr_node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                ans = level
            level += 1
        return ans





