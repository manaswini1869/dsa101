# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempo = oddList = ListNode(float("inf"), None)
        tempe = evenList = ListNode(float("inf"), None)

        idx = 1
        while head:
            if idx % 2 == 0:
                evenList.next = head
                evenList = evenList.next
            else:
                oddList.next = head
                oddList = oddList.next
            head = head.next
            evenList.next = None
            oddList.next = None
            idx += 1
        oddList.next = tempe.next

        return tempo.next



