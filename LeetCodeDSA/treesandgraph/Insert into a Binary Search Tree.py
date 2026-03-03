# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        new_node = TreeNode(val)
        if not root:
            return new_node

        node = root

        while True:

            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    break

            else:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    break

        return root



