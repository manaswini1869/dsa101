# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        init_diff = abs(root.val - target)
        ans = root.val

        node = root
        while node:
            curr_diff = abs(node.val - target)
            if curr_diff < init_diff:
                ans = node.val
                init_diff = curr_diff
            elif curr_diff == init_diff:
                ans = min(ans, node.val)

            if target < node.val:
                node = node.left
            else:
                node = node.right
        return ans












