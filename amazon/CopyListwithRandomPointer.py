"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visited_nodes = {}
    def getCloneNode(self, node):
        if node:
            if node in self.visited_nodes:
                return self.visited_nodes[node]
            else:
                self.visited_nodes[node] = Node(node.val, None, None)
                return self.visited_nodes[node]
        else:
            return None
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if head is None:
        #     return None
        # if head in self.visited_nodes:
        #     return self.visited_nodes[head]

        # node = Node(head.val, None, None)

        # self.visited_nodes[head] = node

        # node.next = self.copyRandomList(head.next)
        # node.random = self.copyRandomList(head.random)

        # return node

        if head is None:
            return None
        old_node = head
        node = Node(old_node.val, None, None)
        self.visited_nodes[old_node] = node

        while old_node != None:
            node.next = self.getCloneNode(old_node.next)
            node.random = self.getCloneNode(old_node.random)
            old_node = old_node.next
            node = node.next
        return self.visited_nodes[head]