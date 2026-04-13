# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        result = []
        curr_path = []
        def dfs(node, curr):
            if node is None:
                return
            curr += node.val
            curr_path.append(node.val)
            
            if node.left is None and node.right is None and curr == targetSum:
                result.append(curr_path[:])
            
            dfs(node.right, curr)
            dfs(node.left, curr)
            curr_path.pop()
        dfs(root, 0)
        return result
            
        


        