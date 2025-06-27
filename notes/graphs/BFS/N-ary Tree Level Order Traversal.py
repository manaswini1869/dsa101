"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:

            level = len(queue)
            current_level = []

            for _ in range(level):
                node = queue.popleft()
                current_level.append(node.val)
                if node.children:
                    for child in node.children:
                        queue.append(child)

            res.append(current_level)

        return res

