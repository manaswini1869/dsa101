# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root, seq):
            if not root:
                return
            if not root.left and not root.right:
                seq.append(root.val)
                return
            dfs(root.left, seq)
            dfs(root.right, seq)
        seq1, seq2 = [], []
        dfs(root1, seq1)
        dfs(root2, seq2)
        return seq1 == seq2

        # time complexity : O(t1+t2) 
        # space complexity : O(l1+l2)



        