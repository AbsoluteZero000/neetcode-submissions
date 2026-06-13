class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        prev = self.reverseKGroup(curr, k)

        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev