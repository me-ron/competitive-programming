class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = -1
        j = len(nums) - 1

        while i + 1 < j:
            mid = (i + j) // 2

            if nums[j] > nums[mid]:
                j = mid
            
            else:
                i = mid
        
        return nums[j]
        