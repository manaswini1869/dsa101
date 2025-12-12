# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return TreeNode()
        n = len(nums)
        mid = n // 2
        root = TreeNode(nums[mid])
        q = deque()
        q.append((root, 0, mid-1))
        q.append((root, mid+1, n-1))
        while q:
            curr, left, right = q.popleft()
            if left <= right:
                mid = (left + right) // 2
                node = TreeNode(nums[mid])
                if node.val < curr.val:
                    curr.left = node
                else:
                    curr.right = node
                q.append((node, left, mid-1))
                q.append((node, mid+1, right))

        return root







