# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=pre
            if curr.next and curr.val>curr.next.val:
                pre=curr.next
            else:
                pre=curr
            key=curr.val
            dum=curr
            while dum.next and key>dum.next.val:
                dum=dum.next
            t=dum.next
            dum.next=curr
            curr.next=t
            curr=temp
        return pre