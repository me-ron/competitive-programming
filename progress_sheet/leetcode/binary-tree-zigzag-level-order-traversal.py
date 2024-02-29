# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def traverse(root, level):
            if not root:
                return
            if level >= len(ans):
                ans.append(deque())
            if level % 2:
                ans[level].appendleft(root.val)
            else:
                ans[level].append(root.val)

            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root, 0)
        return ans