# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        temp=merged
        i=list1
        j=list2
        while i and j:
            if i.val<=j.val:
                temp.next=ListNode(i.val)
                temp=temp.next
                i=i.next
            else:
                temp.next=ListNode(j.val)
                temp=temp.next
                j=j.next


        temp.next=i or j
        return merged.next




        