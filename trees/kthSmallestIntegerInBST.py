# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursively
        # res = []
        # def inorder(node):
        #     if not node:
        #         return None
        #     inorder(node.left)
        #     res.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # return res[k-1]
        #iteratively
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right