# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans=[None for _ in range(k)]
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
        m, r = n//k, n%k
        i=0
        while head:
            ans[i]=head
            j=0
            while head and j < (m + (i < r) - 1):
                head=head.next
                j+=1
            temp=head.next
            if head:
                head.next=None
            head=temp
            i+=1
        return ans
