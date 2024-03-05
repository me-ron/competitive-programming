# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def travel(root, ans):
            if not root:
                return
            travel(root.left, ans)
            ans.append(root.val)
            travel(root.right, ans)

        ans = []
        travel(root, ans)
        return ans

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def create(l, r):
            if r < l:
                return
            if r == l:
                return TreeNode(nums[r])
            
            mid = (l + r)//2
            node = TreeNode(nums[mid])
            node.left = create(l, mid -1)
            node.right = create(mid + 1, r)

            return node
        
        return create(0, len(nums) - 1)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = self.inorderTraversal(root)
        return self.sortedArrayToBST(nums)
        