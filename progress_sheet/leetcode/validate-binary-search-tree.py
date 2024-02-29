# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(root, min_val, max_val):
            if not root:
                return True
            if root.val >= max_val or root.val <= min_val:
                return False
            
            right = help(root.right, root.val, max_val)
            left = help(root.left, min_val,  root.val)
            return left and right

        right = help(root.right, root.val, inf)
        left = help(root.left, -inf, root.val)

        return left and right
        