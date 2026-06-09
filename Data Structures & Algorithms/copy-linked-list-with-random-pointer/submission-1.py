"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {}
       
        newHead = Node(0)
        curr = newHead
        while head:
            curr.next = Node(head.val)
            mp[head] = curr.next
            curr = curr.next
            head = head.next 

        for key in mp:
            mp.get(key).random = mp.get(key.random)
            

        return newHead.next
            