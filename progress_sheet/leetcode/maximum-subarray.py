class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans,temp=nums[0],nums[0]
        i=0
        for j in range(1,len(nums)):
            temp+=nums[j]
            ans=max(ans,temp)
            while i<j and (temp<0 or nums[i]<0):
                temp-=nums[i]
                ans=max(ans,temp) 
                i+=1
                
        return ans
        