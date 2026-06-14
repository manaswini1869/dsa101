# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        if not head:
            return None
        
        temp = []
        curr = node = head
        while node:
            node = node.next
            if node:
                node = node.next
                temp.append(curr.val)
                curr = curr.next
        res = float("-inf")
        for j in temp[::-1]:
            res = max(res, j + curr.val)
            curr = curr.next
        return res
        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        # n = len(arr)
        # res = float("-inf")
        # l, r = 0, n - 1
        # while l < r:
        #     res = max(res, arr[l]+arr[r])
        #     l += 1
        #     r -= 1
        # return res