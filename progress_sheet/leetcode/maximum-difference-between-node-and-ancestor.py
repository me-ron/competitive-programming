# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def diff(node):
            if not node:
                return (inf, -inf)

            left = diff(node.left)
            right = diff(node.right)

            min_val = min(left[0], right[0])
            max_val = max(left[1], right[1])
            if min_val < inf and max_val > -inf:
                self.ans = max(abs(node.val - max_val), abs(node.val - min_val), self.ans)

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            return (min_val, max_val)

        diff(root)
        return self.ans