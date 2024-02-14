# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=set()
        b=set()
        temp_a=headA
        temp_b=headB
        while temp_a or temp_b:

            if temp_a in b or temp_a==temp_b:
                return temp_a
            elif temp_b in a:
                return temp_b

            if temp_b:
                b.add(temp_b)
                temp_b=temp_b.next
            if temp_a:
                a.add(temp_a)
                temp_a=temp_a.next