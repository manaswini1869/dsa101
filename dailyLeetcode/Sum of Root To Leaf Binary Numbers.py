# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        ans = 0
        seen = set()
        def dfs(node, curr):
            nonlocal ans
            if not node:
                return
            
            curr += str(node.val)

            if not node.left and not node.right:
                ans += int(curr, 2)
            
            dfs(node.left, curr)
            dfs(node.right, curr)


        dfs(root, "")

        return ans

        # time complexity : O(h)
        # space complexity : O(h)


        