# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(next=head)
        
        p1=dummy
        p2 = head
        
        while p2:
            
            if p2.val == val:
                p1.next = p2.next
            else:
                p1 = p2
                
            p2 = p2.next
        
        return dummy.next