# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None: 
            nxt = curr.next # before reassigning curr.next
            
            # prev -> curr -> nxt changes to prev <- curr -> nxt
            curr.next = prev 

            # move pointers by one slot
            prev = curr
            curr = nxt

        return prev