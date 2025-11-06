class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        leftPrev = dummy
        for _ in range(left - 1):
            leftPrev = leftPrev.next

        prev = None
        curr = leftPrev.next

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next
