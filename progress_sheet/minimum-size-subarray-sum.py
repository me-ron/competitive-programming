class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        summ=0
        ans=float("inf")
        for j in range(len(nums)):
            summ+=nums[j]
            while summ-nums[i]>=target:
                summ-=nums[i]
                i+=1
            ans=min(ans,j-i) if summ>=target else ans
        return ans+1 if summ>=target else 0