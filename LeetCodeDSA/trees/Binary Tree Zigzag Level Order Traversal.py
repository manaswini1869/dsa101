# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        q = deque([root])
        right = True
        while q:
            level = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            right = not right
            ans.append(list(level))
        return ans











