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
        
        dummy = ListNode(0, head)
        tail = dummy

        while cur:
            cur = cur.next
            tail = tail.next
        
        tail.next = tail.next.next

        return dummy.next