# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

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

        # sorted_arr = []
        # def sort_tree(node):
        #     if not node:
        #         return

        #     sort_tree(node.left)
        #     sorted_arr.append(node.val)
        #     sort_tree(node.right)
        #     return node.val
        # sort_tree(root)
        # return sorted_arr[k-1]


