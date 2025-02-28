# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        def dfs(node, height):
            if not node:
                return node
            if height == len(res):
                res.append(node.val)
            dfs(node.right, height+1)
            dfs(node.left, height+1)
        dfs(cur, 0)
        return res
