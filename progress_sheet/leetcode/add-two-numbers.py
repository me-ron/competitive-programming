# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        ans=ListNode()
        t3=ans
        t1,t2=l1,l2
        while t1 or t2:
            if t1 and t2:
                add=t1.val+t2.val+carry
                carry=add//10
                new=ListNode(add%(10))
                t1=t1.next
                t2=t2.next
            elif t1:
                add=t1.val+carry
                carry=add//10
                new=ListNode(add%(10))
                t1=t1.next
            else:
                add=t2.val+carry
                carry=add//10
                new=ListNode(add%(10))
                t2=t2.next
            t3.next=new
            t3=t3.next 
        if carry:
            t3.next=ListNode(carry) 
        return ans.next
        