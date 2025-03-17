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

def LoopDetection(l1: LinkedList)-> (bool, Node):
    if not l1.head or not l1.head.next:
        return False, None

    slow, fast = l1.head, l1.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return False, None
    slow = l1.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return True, slow


def test_loop_detection():
    # Test Case 1: No loop
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(4)

    result, node = LoopDetection(l1)
    print("Test Case 1 Result: No loop ->", result)
    assert result == False  # Expected: False
    assert node is None  # Expected: None

    # Test Case 2: Loop at the beginning
    l2 = LinkedList()
    l2.append(1)
    l2.append(2)
    l2.append(3)
    l2.append(4)

    loop_node = l2.head  # Creating a cycle at the beginning
    last_node = l2.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = loop_node  # Creating loop

    result, node = LoopDetection(l2)
    print("Test Case 2 Result: Loop at beginning ->", result, "at node with value:", node.data)
    assert result == True  # Expected: True
    assert node.data == 1  # Expected: First node in loop

    # Test Case 3: Loop in the middle
    l3 = LinkedList()
    l3.append(1)
    l3.append(2)
    l3.append(3)
    l3.append(4)
    l3.append(5)

    loop_node = l3.head.next.next  # Creating a cycle at node 3
    last_node = l3.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = loop_node  # Creating loop

    result, node = LoopDetection(l3)
    print("Test Case 3 Result: Loop in middle ->", result, "at node with value:", node.data)
    assert result == True  # Expected: True
    assert node.data == 3  # Expected: Node 3 starts the loop

    # Test Case 4: Loop at the end
    l4 = LinkedList()
    l4.append(1)
    l4.append(2)
    l4.append(3)
    l4.append(4)

    loop_node = l4.head.next.next.next  # Creating a cycle at node 4
    last_node = l4.head
    while last_node.next:
        last_node = last_node.next
    last_node.next = loop_node  # Creating loop

    result, node = LoopDetection(l4)
    print("Test Case 4 Result: Loop at end ->", result, "at node with value:", node.data)
    assert result == True  # Expected: True
    assert node.data == 4  # Expected: Node 4 starts the loop

    # Test Case 5: Single node with loop
    l5 = LinkedList()
    l5.append(1)

    loop_node = l5.head
    loop_node.next = loop_node  # Self-loop

    result, node = LoopDetection(l5)
    print("Test Case 5 Result: Single node loop ->", result, "at node with value:", node.data)
    assert result == True  # Expected: True
    assert node.data == 1  # Expected: Self-loop at node 1

    # Test Case 6: Empty List (No loop)
    l6 = LinkedList()

    result, node = LoopDetection(l6)
    print("Test Case 6 Result: Empty list ->", result)
    assert result == False  # Expected: False
    assert node is None  # Expected: None

# Run all test cases
test_loop_detection()