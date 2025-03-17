from typing import List
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

def remove_duplicate(linked_list: LinkedList) -> List[int]:
    data_list = set()
    dup_data = []
    head = linked_list.head
    while head:
        if head.data in data_list:
            dup_data.append(head.data)
        else:
            data_list.add(head.data)
        head = head.next
    return dup_data

def test_remove_duplicate():
    # **Test Case 1: General Case with Duplicates**
    ll1 = LinkedList()
    for val in [1, 2, 2, 3, 4, 4, 5]:
        ll1.append(val)
    assert remove_duplicate(ll1) == [2, 4]

    # **Test Case 2: No Duplicates**
    ll2 = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll2.append(val)
    assert remove_duplicate(ll2) == []

    # **Test Case 3: All Duplicates**
    ll3 = LinkedList()
    for val in [7, 7, 7, 7, 7]:
        ll3.append(val)
    assert remove_duplicate(ll3) == [7, 7, 7, 7]  # First occurrence is not counted

    # **Test Case 4: Empty List**
    ll4 = LinkedList()
    assert remove_duplicate(ll4) == []

    # **Test Case 5: Single Element List**
    ll5 = LinkedList()
    ll5.append(10)
    assert remove_duplicate(ll5) == []

    # **Test Case 6: Mixed Duplicates**
    ll6 = LinkedList()
    for val in [1, 2, 3, 2, 4, 5, 6, 1, 7, 8, 9, 3]:
        ll6.append(val)
    assert remove_duplicate(ll6) == [2, 1, 3]

    print("All test cases passed!")

test_remove_duplicate()
