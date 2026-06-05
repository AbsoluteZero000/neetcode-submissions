# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        carry = 0
        while l1 and l2:
            total = l1.val + l2.val + carry
            curr.next = ListNode()
            if total >= 10:
                curr.next.val += total-10 
                carry = 1
            else:
                curr.next.val += total 
                carry = 0
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        rem = l1 if l1 else l2
        while rem:
            curr.next = ListNode()
            if rem.val + carry == 10:
                carry = 1
                curr.next.val = 0
            else:
                curr.next = ListNode(rem.val)
                curr.next.val += carry
                carry = 0
            curr = curr.next
            rem = rem.next 
        
        if carry == 1:
            curr.next = ListNode(1)
        
        return head.next
            