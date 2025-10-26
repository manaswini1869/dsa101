# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.right and not root.left):
            return True

        def dfs(node):
            if not node:
                return 0

            left_h = dfs(node.left)
            if left_h == -1:
                return -1

            right_h = dfs(node.right)
            if right_h == -1:
                return -1

            if abs(left_h - right_h) > 1:
                return -1

            return max(left_h, right_h) + 1


        return dfs(root) != -1

