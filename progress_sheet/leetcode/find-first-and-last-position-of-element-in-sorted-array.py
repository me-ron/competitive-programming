class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        i = -1
        j = len(nums) - 1
        ans = [-1, -1]

        while i + 1 < j:
            mid = (i + j) // 2
            
            if nums[mid] == target:
                j = mid 
            elif nums[mid] < target:
                i = mid
            else:
                j = mid - 1
        ans[0] = j if j >= 0 and nums[j] == target else -1

        i = 0
        j = len(nums) 

        while i + 1 < j:
            mid = (i + j) // 2
            if nums[mid] == target:
                i = mid 
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        ans[1] = i if i < len(nums) and nums[i] == target else -1
        
        return ans
        
        