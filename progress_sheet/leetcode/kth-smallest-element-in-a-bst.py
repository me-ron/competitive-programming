# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def smallest(node):
            nonlocal k
            if not node:
                return

            smallest(node.left)
            k -= 1
            if k == 0:
                self.ans = node.val
                return
            smallest(node.right)   

        smallest(root)
        return self.ans             
        