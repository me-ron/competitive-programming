# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        bl=None
        l,r=None,None
        dummy=head
        idx=1
        while dummy:
            if idx==left-1:
                bl=dummy
            elif idx==left:
                l=dummy
                prev=None
                while dummy and idx<=right:
                    if idx==right:
                        r=dummy
                    temp=dummy.next
                    dummy.next=prev
                    prev=dummy
                    dummy=temp
                    idx+=1
                l.next=dummy
                break
            dummy=dummy.next
            idx+=1
        if bl:
            bl.next=r
        else: 
            head=r
        return head