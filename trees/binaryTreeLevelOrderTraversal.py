# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(cur, height):
            if not cur:
                return None
            if(len(res) == height):
                res.append([])
            res[height].append(cur.val)
            dfs(cur.left, height+1)
            dfs(cur.right, height+1)
        dfs(root, 0)
        return res