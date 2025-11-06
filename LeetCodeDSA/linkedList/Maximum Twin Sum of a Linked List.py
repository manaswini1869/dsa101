# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        if not head or not head.next:
            return head.val

        new_head = head

        slow = fast = new_head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        max_sum = float("-inf")

        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev
        first = head

        max_sum = 0
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum


