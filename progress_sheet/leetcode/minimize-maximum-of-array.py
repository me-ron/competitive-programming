class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        run = 0
        for i in range(len(nums)):
            run += nums[i]
            ans = max(ans, ceil(run/(i+1)))
            
        return ans
        
        