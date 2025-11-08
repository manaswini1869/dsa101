# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        slow = fast = head

        for _ in range(k-1):
            fast = fast.next

        first = fast

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.val, first.val = first.val, slow.val
        return head




