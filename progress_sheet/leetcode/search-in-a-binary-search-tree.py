# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root, num):
            if not root:
                return 
            if num == root.val:
                return root
            elif num < root.val:
                return search(root.left, num)
            else:
                return search(root.right, num)
        if not root:
            return root
        return search(root, val)