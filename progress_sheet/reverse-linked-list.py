# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before=None
        after=head
        while after!=None:
            temp=after.next
            after.next=before
            before=after
            after=temp
        return before
