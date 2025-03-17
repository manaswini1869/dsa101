class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

def Partition(linked_list: LinkedList, x: int):
    left_head = left = Node(0)
    right_head = right = Node(0)
    current = linked_list.head

    while current:
        if current.data < x:
            left = current.data
            left = left.next
        else:
            right = current.data
            right = right.next
        current = current.next
    right.next = None
    left.next = right_head.head
    linked_list.head = left_head.next
