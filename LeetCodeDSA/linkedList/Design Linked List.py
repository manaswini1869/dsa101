class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        temp = self.head
        i = 0
        while temp:
            if i == index:
                return temp.val
            temp = temp.next
            i += 1
        return -1


    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def addAtTail(self, val: int) -> None:
        tmp = Node(val)
        if not self.head:
            self.head = tmp
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = tmp

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        tmp = Node(val)
        temp = self.head

        i = 0
        while temp and i < index - 1:
            temp = temp.next
            i += 1
        if not temp:
            return
        tmp.next = temp.next
        temp.next = tmp


    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        i = 0
        while temp and i < index - 1:
            temp = temp.next
            i += 1

        if not temp or not temp.next:
            return

        temp.next = temp.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)