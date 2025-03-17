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

def reverse(l: LinkedList) -> LinkedList:
    prev = None
    current = l.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    reversed_list = LinkedList()
    reversed_list.head = prev
    return reversed_list

def Palindrome(l1: LinkedList) -> bool:
    l1_rev = reverse(l1)
    h1, h2 = l1.head, l1_rev.head
    while h1 and h2:
        if h1.data != h2.data:
            return False
        h1 = h1.next
        h2 = h2.next
    return True

def test_palindrome():
    # Test Case 1: Palindrome List
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(2)
    l1.append(1)

    result = Palindrome(l1)
    print("Test Case 1 Result: Palindrome List ->", result)
    assert result == True  # Expected: True

    # Test Case 2: Non-Palindrome List
    l2 = LinkedList()
    l2.append(1)
    l2.append(2)
    l2.append(3)

    result = Palindrome(l2)
    print("Test Case 2 Result: Non-Palindrome List ->", result)
    assert result == False  # Expected: False

    # Test Case 3: Single Element List (Palindrome by default)
    l3 = LinkedList()
    l3.append(1)

    result = Palindrome(l3)
    print("Test Case 3 Result: Single Element List ->", result)
    assert result == True  # Expected: True

    # Test Case 4: Empty List (Palindrome by default)
    l4 = LinkedList()

    result = Palindrome(l4)
    print("Test Case 4 Result: Empty List ->", result)
    assert result == True  # Expected: True

    # Test Case 5: Palindrome List with even number of elements
    l5 = LinkedList()
    l5.append(1)
    l5.append(2)
    l5.append(2)
    l5.append(1)

    result = Palindrome(l5)
    print("Test Case 5 Result: Palindrome List (Even Length) ->", result)
    assert result == True  # Expected: True

    # Test Case 6: Non-Palindrome List with even number of elements
    l6 = LinkedList()
    l6.append(1)
    l6.append(2)
    l6.append(3)
    l6.append(4)

    result = Palindrome(l6)
    print("Test Case 6 Result: Non-Palindrome List (Even Length) ->", result)
    assert result == False  # Expected: False

# Run all test cases
test_palindrome()
