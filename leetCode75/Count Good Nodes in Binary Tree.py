# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 1
        count_good = 0
        def dfs(node, max_so):
            nonlocal count_good
            if max_so <= node.val:
                count_good += 1
            if node.right:
                dfs(node.right, max(node.val, max_so))
            if node.left:
                dfs(node.left, max(node.val, max_so))
        dfs(root, float('-inf'))
        return count_good