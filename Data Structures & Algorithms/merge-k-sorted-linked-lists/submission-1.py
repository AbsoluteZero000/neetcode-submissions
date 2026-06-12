# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newList = ListNode()
        newHead = newList

        while True:
            minNode = ListNode(10000)
            minIndex = -1
            for i in range(len(lists)):
                node = lists[i]
                if node: 
                    if minNode.val > node.val:
                        minNode = node
                        minIndex = i

            if minIndex == -1:
                return newHead.next

            lists[minIndex] = lists[minIndex].next
            newList.next = minNode
            newList = newList.next

        return newHead.next


                        

                    

        