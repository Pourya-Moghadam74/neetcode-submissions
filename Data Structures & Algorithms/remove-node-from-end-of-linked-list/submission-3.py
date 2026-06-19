class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        count = 0
        while end and end.next:
            end = end.next
            count += 1
        
        # count represents the length of the list minus 1
        total_nodes = count + 1
        num = total_nodes - n
        
        if num == 0:
            return head.next

        cur = head
        for i in range(num):
            if (i + 1) == num:
                cur.next = cur.next.next
                break
            cur = cur.next
        
        return head