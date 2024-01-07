class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=sub=sum(nums[:k])
        for i in range(k,len(nums)):
            sub+=nums[i]-nums[i-k]
            ans=max(ans,sub)
        return ans/k
