# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursionTree(self, node, remainigSum, pathNodes, pathList):
        if not node:
            return
        pathNodes.append(node.val)
        if remainigSum == node.val and not node.left and not node.right:
            pathList.append(list(pathNodes))
        else:
            self.recursionTree(node.left, remainigSum - node.val, pathNodes, pathList)
            self.recursionTree(node.right, remainigSum - node.val, pathNodes, pathList)
        pathNodes.pop()
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        pathList = []
        self.recursionTree(root, targetSum, [], pathList)
        return pathList
