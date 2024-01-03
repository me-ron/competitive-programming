class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans+=(nums[i]+nums[j]<target)
        return ans
