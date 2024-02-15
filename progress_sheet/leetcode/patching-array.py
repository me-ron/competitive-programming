class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, i, cover = 0, 0, 0
        while cover < n:
            if i < len(nums) and nums[i] <= cover + 1:
                cover += nums[i]
                i += 1
            else:
                cover += cover + 1
                patches += 1
        return patches
            

        