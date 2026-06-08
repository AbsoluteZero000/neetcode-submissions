# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        curr = head
        tmp = n
        while curr and tmp > 0:
            curr = curr.next
            tmp-=1

        prev = head

        if not curr:
            return head.next
        
        curr = curr.next
        while curr:
            prev = prev.next
            curr = curr.next
        
        prev.next = prev.next.next

        return head