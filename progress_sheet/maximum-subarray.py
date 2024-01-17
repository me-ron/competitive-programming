class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans,temp=float("-inf"),0
        i=0
        for j in range(len(nums)):
            if j!=0:
                nums[j]+=nums[j-1]
            ans=max(nums[j]-temp,ans)
            temp=min(nums[j],temp)
           
        return ans
        