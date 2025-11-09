# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return True

        temp = slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True




