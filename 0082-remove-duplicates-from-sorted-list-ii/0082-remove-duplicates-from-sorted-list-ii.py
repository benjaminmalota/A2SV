# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(next=head)
        pointer = dummy 
        
        while pointer:
            if pointer.next and pointer.next.next and pointer.next.val == pointer.next.next.val:
                node = pointer.next
                while node and node.next and node.next.val == node.val:
                    node = node.next
                pointer.next = node.next
            else:
                pointer = pointer.next
        return dummy.next
                        
                    