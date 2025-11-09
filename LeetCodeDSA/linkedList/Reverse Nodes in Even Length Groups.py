# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dum = ListNode(0, head)
        curr = head
        prev = dum

        grp = 1

        while curr:
            count = 0
            node = curr

            while node and count < grp:
                node = node.next
                count += 1

            if count % 2 == 0:
                prev_nxt = prev.next
                next_grp_head = node

                prev_node = next_grp_head
                temp = curr

                for _ in range(count):
                    nxt = temp.next
                    temp.next = prev_node
                    prev_node = temp
                    temp = nxt

                prev.next = prev_node
                prev = prev_nxt
                curr = next_grp_head
            else:
                for _ in range(count):
                    prev = curr
                    curr = curr.next
            grp += 1





        return dum.next







        # if not head or not head.next:
        #     return head

        # count = 1

        # node_vals= []
        # while head:
        #     node_vals.append(head.val)
        #     head = head.next

        # n = len(node_vals)
        # mapper = defaultdict(list)
        # grp_id = 1
        # i = 0

        # while i < n:
        #     take = min(grp_id, n - i)
        #     mapper[grp_id] = node_vals[i:i+take]
        #     i += take
        #     grp_id += 1

        # for k, v in mapper.items():
        #     if len(v) % 2 == 0:
        #         mapper[k].reverse()

        # dummy = new_head = ListNode(0)

        # for v in mapper.values():
        #     for i in v:
        #         new_head.next = ListNode(i)
        #         new_head = new_head.next

        # return dummy.next









