# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        bl, ar = None, None
        l, r = None, None
        dummy = head
        idx = 1
        while dummy:
            if idx == left - 1:
                bl = dummy
            elif idx == left:
                l = curr = dummy
                prev = None
                while curr and idx <= right:
                    if idx == right:
                        r = curr
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                    idx += 1
                l.next = curr
            dummy = dummy.next
            idx += 1
        if bl:
            bl.next = r
        else:
            head = r
        return head