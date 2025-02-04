# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        n = n//2 if n%2!=0 else ceil(n/2)
        print(n)
        while n >0:
            head = head.next
            n -= 1
        return head