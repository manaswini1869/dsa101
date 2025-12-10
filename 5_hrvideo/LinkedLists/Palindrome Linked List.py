# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        start = slow
        prev = None
        while start:
            nxt = start.next
            start.next = prev
            prev = start
            start = nxt

        while prev:
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next
        return True



