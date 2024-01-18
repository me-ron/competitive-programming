class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        ans=[0]*len(nums)
        for a,b in requests:
            ans[a]+=1
            if b+1<len(nums):
                ans[b+1]-=1
        for i in range(1,len(nums)):
            ans[i]+=ans[i-1]

        ans.sort()
        res=0
        for i in range(len(nums)):
            res+=nums[i]*ans[i]
        return res%(10**9 + 7)
    