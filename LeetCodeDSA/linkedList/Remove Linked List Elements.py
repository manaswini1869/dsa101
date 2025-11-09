# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dum = ListNode(float("inf"), head)
        prev = dum

        temp = head

        while temp:
            if temp.val == val:
                if temp.next:
                    prev.next = temp.next
                else:
                    prev.next = None
                temp = temp.next

            else:
                prev = temp
                temp = temp.next


        return dum.next


