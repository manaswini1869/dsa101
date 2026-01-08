# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9+7
        max_prod = 0

        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.right) + total_sum(node.left)

        tree_sum = total_sum(root)

        def subtree_sum(node):
            nonlocal max_prod
            if not node:
                return 0
            left = subtree_sum(node.left)
            right = subtree_sum(node.right)
            curr_sum = node.val + left + right

            max_prod = max(max_prod, curr_sum*(tree_sum-curr_sum))

            return curr_sum

        subtree_sum(root)


        return max_prod % MOD
