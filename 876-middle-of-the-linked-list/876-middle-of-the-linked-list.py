# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        counter = 0
        while node:
            counter += 1
            node=node.next
        index = counter//2
        node = head
        for i in range(index):
            node = node.next
        return node
        
        
            
        