# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new=ListNode()
        new.next=head
        dum=head
        while dum:
            n-=1
            dum=dum.next
        temp=new
        while temp:
            if n==0:
                temp.next=temp.next.next
                return new.next
            n+=1
            temp=temp.next
