# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_head = head
        curr = head
        if curr is None or curr.next is None:
            return curr
        nxt = curr.next
        head.next = None
        while nxt is not None: 
            nxt2 = nxt.next
            # curr -> nxt -> nx2 becomes curr <- nxt   nxt2 -> nxt3
            nxt.next = curr
            curr = nxt
            nxt = nxt2

        return curr

# 1. values are 0 1, next iteration values are 1, 2, update next connection of 0, 1
#
