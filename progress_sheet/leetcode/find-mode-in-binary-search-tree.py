# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def find(root, dup):
            if not root:
                return 
            dup[root.val] += 1
            find(root.left, dup)
            find(root.right, dup)

        dup = defaultdict(int)
        find(root, dup)

        ans = max(dup.values())
        return [i for i in dup if dup[i] == ans]