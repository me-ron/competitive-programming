# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hold=ans=head
        if not hold:
            return head
        seek=head.next
        while seek:
            if seek.val!=hold.val:
                hold.next=seek
                hold=hold.next
            seek=seek.next
        hold.next=seek
        return ans



        