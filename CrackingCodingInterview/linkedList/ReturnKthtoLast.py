class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

def KthToLast(linked_list: LinkedList, k: int) -> int:
    if k <= 0:
        raise ValueError("k should be a positive integer")

    res, ref = linked_list.head, linked_list.head
    # Move ref k steps ahead
    for _ in range(k):
        if ref is None:
            raise ValueError(f"k={k} is larger than the size of the linked list")
        ref = ref.next

    # Move both pointers one step at a time
    while ref:
        res = res.next
        ref = ref.next

    return res.data

def test_KthToLast():
    # Case 1: General Case with multiple elements
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(4)
    ll1.append(5)
    print(KthToLast(ll1, 5))  # Expected: 1 (first element)
    assert KthToLast(ll1, 1) == 5  # Last element
    assert KthToLast(ll1, 2) == 4  # Second to last element
    assert KthToLast(ll1, 3) == 3  # Third to last element
    assert KthToLast(ll1, 5) == 1  # First element

    # Case 2: Case where k is greater than the size of the list
    try:
        KthToLast(ll1, 6)
    except ValueError as e:
        assert str(e) == "k=6 is larger than the size of the linked list"

    # Case 3: Case where k <= 0 (Invalid k)
    try:
        KthToLast(ll1, 0)
    except ValueError as e:
        assert str(e) == "k should be a positive integer"

    # Case 4: Empty list
    ll2 = LinkedList()
    try:
        KthToLast(ll2, 1)
    except ValueError as e:
        assert str(e) == "k=1 is larger than the size of the linked list"

    # Case 5: Single element list
    ll3 = LinkedList()
    ll3.append(10)
    assert KthToLast(ll3, 1) == 10  # Only one element

    # Case 6: k is exactly the size of the list
    ll4 = LinkedList()
    ll4.append(1)
    ll4.append(2)
    ll4.append(3)
    ll4.append(4)
    ll4.append(5)
    assert KthToLast(ll4, 5) == 1  # First element (k == list size)

    print("All test cases passed!")

# Run the test cases
test_KthToLast()
