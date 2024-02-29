# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def sums(node, digits):
            if not node:
                return
            if not node.left and not node.right:
                ans.append(digits * 10 + node.val)
                return
             
            if node.left:
                sums(node.left, digits * 10 + node.val)
            if node.right:
                sums(node.right, digits * 10 + node.val)

        sums(root, 0)
        return sum(ans)