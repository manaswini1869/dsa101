# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        if not nums:
            return head
        nums = set(nums)
        new_head = tmp = ListNode(0)
        while head:
            if head.val not in nums:
                tmp.next = ListNode(head.val)
                tmp = tmp.next
            head = head.next
        return new_head.next





        # while head:
        #     new_list.append(head.val)
        #     head = head.next

        # for num in nums:
        #     while num in new_list:
        #         new_list.remove(num)

        # new_head = ListNode(new_list[0])
        # temp = new_head

        # for i in new_list[1:]:
        #     temp.next = ListNode(i)
        #     temp = temp.next

        # return new_head




