# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        sorted_arr = []

        def inorder(dumm):
            if not dumm:
                return
            inorder(dumm.left)
            sorted_arr.append(dumm.val)
            inorder(dumm.right)

        inorder(root)

        n = len(sorted_arr)
        mid = n // 2
        new_root = TreeNode(sorted_arr[mid])
        q = deque()
        q.append((new_root, 0, mid-1))
        q.append((new_root, mid+1, n-1))

        while q:
            curr, left, right = q.popleft()
            if left <= right:
                mid = (left + right) // 2
                node = TreeNode(sorted_arr[mid])
                if node.val < curr.val:
                    curr.left = node
                else:
                    curr.right = node
                q.append((node, left, mid-1))
                q.append((node, mid+1, right))
        return new_root
