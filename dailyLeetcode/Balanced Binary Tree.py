# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root or (not root.left and not root.right):
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
            
            return max(left_h, right_h)+1

    


        return dfs(root) != -1
        
        # time complexity = O(n) n = number of nodes in the tree
        # space complexity = O(h) h = height of the tree, due to the recusrive stack calculation




        