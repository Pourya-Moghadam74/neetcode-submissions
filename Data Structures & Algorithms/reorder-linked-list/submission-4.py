# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        mid = slow.val
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        start = head
        end = prev

        while end.val != mid:
            next_start = start.next
            next_prev = end.next
            
            start.next = end
            end.next = next_start
            start = next_start
            end = next_prev

        