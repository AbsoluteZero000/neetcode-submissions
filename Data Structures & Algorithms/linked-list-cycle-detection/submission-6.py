# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr = head
        curr_fast = head.next
        
        while curr and curr_fast and curr_fast.next and curr.val != curr_fast.val:
            curr = curr.next
            curr_fast = curr_fast.next.next

        if not curr_fast or not curr_fast.next or not curr:
            return False
        return True
        