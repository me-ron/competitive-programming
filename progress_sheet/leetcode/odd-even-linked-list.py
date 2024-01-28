# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        dum1=head
        even=dum2=head.next
        while dum1.next and dum2.next:
            dum1.next=dum2.next
            dum2.next=dum2.next.next
            dum1=dum1.next
            dum2=dum2.next
        dum1.next=even
        return head
            