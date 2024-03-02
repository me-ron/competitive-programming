# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def helper(root, min_val, max_val):
            if not root:
                return (inf,-inf, 0)
            
            left = helper(root.left, min_val, root.val)
            right = helper(root.right, root.val, max_val)
            
            if left[1] < root.val < right[0]:
                curr_sum = left[2] + right[2] + root.val
                self.result = max(self.result, curr_sum)
                return (min(left[0], root.val), max(right[1], root.val), curr_sum)
            else:
                return (-inf, inf, 0)
        
        helper(root, -inf, inf)
        return self.result
