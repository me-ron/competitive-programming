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
            
            left_min, left_max, left_sum = helper(root.left, min_val, root.val)
            right_min, right_max, right_sum = helper(root.right, root.val, max_val)
            
            if left_max < root.val < right_min:
                curr_sum = left_sum + right_sum + root.val
                self.result = max(self.result, curr_sum)
                return (min(left_min, root.val), max(right_max, root.val), curr_sum)
            else:
                return (-inf, inf, 0)
        
        helper(root, -inf, inf)
        return self.result
