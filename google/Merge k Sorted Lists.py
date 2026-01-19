# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        n = len(lists)
        if not lists or not n:
            return

        merged = lists[0]

        for l2 in lists[1:]:
            curr = temp = ListNode(-1)
            a = merged
            b = l2

            while a and b:
                if b.val < a.val:
                    curr.next = b
                    b = b.next
                else:
                    curr.next = a
                    a = a.next
                curr = curr.next
            if a:
                curr.next = a
            if b:
                curr.next = b
            merged = temp.next

        return merged




