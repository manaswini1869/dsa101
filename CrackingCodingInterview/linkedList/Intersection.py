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

def Intersection(l1: LinkedList, l2: LinkedList) -> (bool, Node):
    h1 = l1.head
    while h1:
        h2 = l2.head
        while h2:
            if h1 == h2:  # If the nodes are the same (intersection point)
                return True, h1
            h2 = h2.next
        h1 = h1.next
    return False, None

def test_intersection():
    # Test Case 1: No intersection
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)

    l2 = LinkedList()
    l2.append(4)
    l2.append(5)

    result, node = Intersection(l1, l2)
    print("Test Case 1 Result: No intersection ->", result)
    assert result == False  # Expected: False
    assert node == None  # Expected: None

    # Test Case 2: Intersection at the start of the list
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    intersection_node = Node(3)  # Intersection node
    l1.head.next.next = intersection_node
    l1.append(4)

    l2 = LinkedList()
    l2.head = intersection_node  # List l2 starts at the intersection node

    result, node = Intersection(l1, l2)
    print("Test Case 2 Result: Intersection at start ->", result, node.data)
    assert result == True  # Expected: True
    assert node.data == 3  # Expected: Intersection node data = 3

    # Test Case 3: Intersection in the middle of the list
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    intersection_node = Node(3)  # Intersection node
    l1.head.next.next = intersection_node
    l1.append(4)

    l2 = LinkedList()
    l2.append(5)
    l2.append(6)
    l2.head.next.next = intersection_node  # List l2 intersects at node 3

    result, node = Intersection(l1, l2)
    print("Test Case 3 Result: Intersection in the middle ->", result, node.data)
    assert result == True  # Expected: True
    assert node.data == 3  # Expected: Intersection node data = 3

    # Test Case 4: Intersection at the end of the list
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    intersection_node = Node(3)  # Intersection node
    l1.head.next.next = intersection_node

    l2 = LinkedList()
    l2.append(4)
    l2.head.next = intersection_node  # List l2 intersects at the end node 3

    result, node = Intersection(l1, l2)
    print("Test Case 4 Result: Intersection at the end ->", result, node.data)
    assert result == True  # Expected: True
    assert node.data == 3  # Expected: Intersection node data = 3

    # Test Case 6: Empty lists (No intersection)
    l1 = LinkedList()
    l2 = LinkedList()

    result, node = Intersection(l1, l2)
    print("Test Case 6 Result: Empty Lists ->", result)
    assert result == False  # Expected: False
    assert node == None  # Expected: None

# Run all test cases
test_intersection()
