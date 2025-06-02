# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        temp = head
        while temp:
            for _ in range(m-1):
                if not temp:
                    return head
                temp = temp.next
            if not temp or not temp.next:
                break
            dele = temp.next
            for _ in range(n):
                if not dele:
                    break
                dele = dele.next
            temp.next = dele
            temp = dele
        return head