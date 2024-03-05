# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def help(nums):
            if not nums:
                return

            max_val = max(nums)
            idx = nums.index(max_val)
            node = TreeNode(max_val)

            node.left = help(nums[:idx])
            node.right = help(nums[idx + 1:])

            return node
        
        return help(nums)