# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        def vertical(node, level, height):
            if not node:
                return
            while height >= len(ans[level]):
                ans[level].append([])

            ans[level][height].append(node.val)
            vertical(node.left, level - 1, height + 1)
            vertical(node.right, level + 1, height + 1)

        vertical(root, 0, 0)
        sorted_keys = sorted(ans.keys())
        result = []
        for key in sorted_keys:
            temp = []
            for val in ans[key]:
                if val:
                    temp += sorted(val)

            result.append(temp)

        return result
        