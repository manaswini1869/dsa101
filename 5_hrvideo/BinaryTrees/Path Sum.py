# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        stack = [(root, root.val)]
        while stack:
            curr, curr_val = stack.pop()
            if not curr.left and not curr.right and curr_val == targetSum:
                return True
            if curr.left:
                stack.append((curr.left, curr_val+curr.left.val))
            if curr.right:
                stack.append((curr.right, curr_val+curr.right.val))



        return False




