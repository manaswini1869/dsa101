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

def DeleteMiddleNode(linked_list: LinkedList):

    if linked_list.head is None or linked_list.head.next is None or linked_list.head.next.next is None:
        return -1

    slow, fast = linked_list.head, linked_list.head
    prev = slow

    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

def test_DeleteMiddleNode():
    # Case 1: General Case with multiple elements
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(4)
    ll1.append(5)
    DeleteMiddleNode(ll1)
    # After deletion, the list should be [1, 2, 4, 5]
    current = ll1.head
    result = []
    while current:
        result.append(current.data)
        current = current.next
    assert result == [1, 2, 4, 5]

    # Case 2: Case with only 3 elements
    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    DeleteMiddleNode(ll2)
    # After deletion, the list should be [10, 30]
    current = ll2.head
    result = []
    while current:
        result.append(current.data)
        current = current.next
    assert result == [10, 30]

    # Case 3: Case with only 2 elements (can't delete middle)
    ll3 = LinkedList()
    ll3.append(100)
    ll3.append(200)
    assert DeleteMiddleNode(ll3) == -1  # Cannot delete the middle node in a list of 2 elements

    # Case 4: Case with a single element (can't delete middle)
    ll4 = LinkedList()
    ll4.append(1)
    assert DeleteMiddleNode(ll4) == -1  # Cannot delete the middle node in a list of 1 element

    # Case 5: Empty list (can't delete middle)
    ll5 = LinkedList()
    assert DeleteMiddleNode(ll5) == -1  # Cannot delete the middle node in an empty list

    print("All test cases passed!")

# Run the test cases
test_DeleteMiddleNode()
