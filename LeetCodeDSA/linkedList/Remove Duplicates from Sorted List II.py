 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dum = ListNode(float("inf"), head)
        prev = dum
        temp = head

        while temp:
            while temp.next and temp.val == temp.next.val:
                temp = temp.next

            if prev.next == temp:
                prev = prev.next
            else:
                prev.next = temp.next
            temp = temp.next
        return dum.next

