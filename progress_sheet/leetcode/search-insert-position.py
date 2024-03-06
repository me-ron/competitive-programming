class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = - 1
        j = len(nums)

        while i + 1 < j:
            mid = (i + j) // 2

            if nums[mid] >= target:
                j = mid
            else:
                i = mid
            
        return j
        