# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reve = None
        temp = head
        while temp:
            node = ListNode(temp.val)
            node.next = reve
            reve = node
            temp = temp.next

        i=head
        j=reve
        while i!=None and j!=None:
            if i.val!=j.val:
                return False
            i=i.next
            j=j.next
        return True