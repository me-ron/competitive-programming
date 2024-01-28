# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dum1=bef=ListNode()
        dum2=af=ListNode()
        while head:
            if head.val<x:
                dum1.next=head
                dum1=dum1.next
            else:
                dum2.next=head
                dum2=dum2.next
                
            head=head.next

        dum1.next=af.next
        dum2.next=None
        return bef.next
        