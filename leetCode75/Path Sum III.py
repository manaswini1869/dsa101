# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return
            curr_sum += node.val
            if curr_sum == k:
                count += 1
            count += hash_sum[curr_sum - k]
            hash_sum[curr_sum] += 1
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            hash_sum[curr_sum] -= 1
        hash_sum = defaultdict(int)
        count, k = 0, targetSum
        preorder(root, 0)
        return count
