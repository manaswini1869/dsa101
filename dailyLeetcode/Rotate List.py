# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        k = k % n
        temp = arr[-k:] + arr[:-k] if k else arr
        res = ListNode()
        ans = res
        for num in temp:
            res.next = ListNode(num)
            res = res.next
        return ans.next



        