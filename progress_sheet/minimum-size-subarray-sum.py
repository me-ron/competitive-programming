class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        summ=0
        ans=float("inf")
        for j in range(len(nums)):
            summ+=nums[j]
            while summ>=target:
                summ-=nums[i]
                ans=min(ans,j-i+1)
                i+=1
        return ans if ans!=float("inf") else 0