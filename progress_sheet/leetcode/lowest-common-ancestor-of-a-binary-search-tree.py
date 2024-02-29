# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root, num1, num2):
            if num1 <= root.val <= num2:
                return root
            if num2 < root.val:
                return search(root.left, num1, num2)
            elif num1 > root.val:
                return search(root.right, num1, num2)

        num1 = min(p.val, q.val)
        num2 = max(p.val, q.val)

        return search(root, num1, num2)