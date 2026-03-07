from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root.left and not root.right:
            return True

        q = deque([root, root])
        while q:
            t1, t2 = q.popleft(), q.popleft()
            if t1 is None and t2 is None:
                continue
            if (t1 and not t2) or (t2 and not t1):
                return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True


        