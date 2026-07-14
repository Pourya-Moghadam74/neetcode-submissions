# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        while n > 0:
            cur = cur.next
            n -= 1
        
        dummy = ListNode(next=head)
        tail = dummy

        first = tail
        while cur:
            cur = cur.next
            first = first.next
        
        first.next = first.next.next

        return dummy.next
