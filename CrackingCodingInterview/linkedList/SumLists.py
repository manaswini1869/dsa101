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

def SumLists(l1: LinkedList, l2: LinkedList) -> int:
    l3 = Node(0)
    head = l3
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.data if l1 else 0
        v2 = l2.data if l2 else 0
        su = v1 + v2 + carry
        val = su % 10
        carry = su // 10
        l3.next = Node(val)
        l3 = l3.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return head.next

def test_sum_lists():
    # Test Case 1: Simple Case Without Carry
    l1 = LinkedList()
    l1.append(7)
    l1.append(1)
    l1.append(6)

    l2 = LinkedList()
    l2.append(5)
    l2.append(9)
    l2.append(2)

    result = SumLists(l1.head, l2.head)
    print("Test Case 1 Result:")
    while result:
        print(result.data, end=" -> " if result.next else "\n")
        result = result.next
    assert result is None  # Expected result: 2 -> 1 -> 9

    # Test Case 2: Case with Carry
    l1 = LinkedList()
    l1.append(9)
    l1.append(9)
    l1.append(9)

    l2 = LinkedList()
    l2.append(1)
    l2.append(1)
    l2.append(1)

    result = SumLists(l1.head, l2.head)
    print("Test Case 2 Result:")
    while result:
        print(result.data, end=" -> " if result.next else "\n")
        result = result.next
    assert result is None  # Expected result: 0 -> 1 -> 1 -> 1

    # Test Case 3: Different Lengths
    l1 = LinkedList()
    l1.append(7)
    l1.append(1)

    l2 = LinkedList()
    l2.append(9)
    l2.append(9)
    l2.append(9)

    result = SumLists(l1.head, l2.head)
    print("Test Case 3 Result:")
    while result:
        print(result.data, end=" -> " if result.next else "\n")
        result = result.next
    assert result is None  # Expected result: 6 -> 1 -> 0 -> 1

    # Test Case 4: One List is Empty
    l1 = LinkedList()
    l1.append(7)
    l1.append(1)

    l2 = LinkedList()  # Empty list

    result = SumLists(l1.head, l2.head)
    print("Test Case 4 Result:")
    while result:
        print(result.data, end=" -> " if result.next else "\n")
        result = result.next
    assert result is None  # Expected result: 7 -> 1

    # Test Case 5: Both Lists are Empty
    l1 = LinkedList()  # Empty list
    l2 = LinkedList()  # Empty list

    result = SumLists(l1.head, l2.head)
    print("Test Case 5 Result:")
    if result:
        while result:
            print(result.data, end=" -> " if result.next else "\n")
            result = result.next
    else:
        print("Empty list")
    assert result is None  # Expected result: Empty list

    # Test Case 6: Single Element Lists
    l1 = LinkedList()
    l1.append(2)

    l2 = LinkedList()
    l2.append(5)

    result = SumLists(l1.head, l2.head)
    print("Test Case 6 Result:")
    while result:
        print(result.data, end=" -> " if result.next else "\n")
        result = result.next
    assert result is None  # Expected result: 7


# Run all test cases
test_sum_lists()